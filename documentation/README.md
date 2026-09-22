1. Indexing starts at 0
2. commas aren't necessary in command parameters
## Data types
`Sprite`; `Player`\
Sprites in the project, including the stage.

`Variable/Var`; `MyVariable.v`\
Any variable from inside the project, but typically referring to local variables. The method of using a variable as input can also be used to refer to it's name, you could use `MyVariable.v` when getting it's name, not just it's data *(unless specified otherwise)*.

`Comp variable/Cvar`; `comp_var.c`\
A variable only existing in the patching process, can be read all throughout your patch, and other patches if specified. Same as variables, the method of using comp variables as input can also be used to refer to it's name, you could use `comp_var.c` when getting it's name, not just it's data *(unless specified otherwise)*.

`String/Str`; `"I'm a string!"`\
Any ascii characters in whatever order.

`Value/Val`; `32`\
Any integer or float number. Inputs like Infinity, -Infinity, and even -0 work too.

`Boolean/Bool`; `True`\
A True or False, on certain occasions, 0 and 1 will work too.

`Any`; `"I'm a string, but I could be anything!"`\
Could be any type of data; value, boolean, string, whatever works.

`Metadata/Meta`; `IsStage?`\
The metadata of a specified item, it's relavent to whatever the metadata is asked from, if it's a sprite then it might be things like it's position, visibilty, size, etc... It's important you know what metadata elements like those have, SCI should inform you about those though.

`Array`, `Object`; `[0, 1]`, `{"key": "data"}`\
A JSON array or object, typically asking for multiple items of data in one input.

`Opcode`; `event_flag`\
A block's opcode, typically used for patching in blocks into script.

`Label`; `Loop:`\
A label is like a marker, using the simple `JUMP` commands, you can easilly jump to them and execute whatever code is below it.

`File`; `M:/assets/NewCostume1`\
A file address, `M:/` being the root of your mod/patch's folder.

`URL`; `https://turbowrap.org`\
A website URL, mainly used for importing extensions.

## Sprites
`SPRITE` `sprite`sprite\
Selects a sprite to where all edits will be made.\
`SPRITE_GET` `sprite`sprite, `out`(c)var\
Gets the name of the currently loaded sprite.

## Write
### Variables
`VAR_WRITE` `variable`var, `data`any\
Writes data to a variable, local and global. If the variable doesn't exist, it's created locally.\
`VAR_GLB` `variable`var, `data`any\
Creates a global variable for if you want to create a global variable instead of a local one.

### Comp Variables
`VAR_COMP` `comp variable`cvar, `data`any\
Overwrites the data of any comp variable, creates a comp variable if it doesn't exist already.

### Metadata
`SPRITE_WRITE` `metadata`meta, `data`any\
Overwrites any metadata from the loaded sprite.\
`PROJECT_WRITE` `metadata`meta, `data`any\
Overwrites any metadata from the project.

## Read
### Variables
`VAR_GLB` `variable`var, `get`get, `out`(c)var\
Write `get` on the `data` parameter of the `VAR_GLB` command to read a global variable. The third parameter is for an output variable.

### Metadata
`SPRITE_READ` `metadata`meta, `out`(c)var\
Read metadata from the loaded sprite and write it into any variable.\
`PROJECT_READ` `metadata`meta, `out`(c)var\
Read metadata from the project and write it into any variable.

## Blocks
### Simple
`BLOCK_SIM` `variable`(c)var, `family`array\
Use the `BLOCK;` command to save a block to a variable, and use it here to patch-it in. Use the array input to specify the parent and child.\
`BLOCK;` `opcode`opcode, `out`(c)var\
Use to save a block to a variable, example:
```bash
BLOCK; motion_goto(0,0), TempBlock.c
# the motion block would be saved to `TempBlock.c`
```
`BLOCK_GET` `metadata`meta, `ID`any\
Read any block's metadata, you can get any block's ID via SCI.
>**Note:** placing a block where one already excists will simply overwrite the old spot with the new block.

### Multiple
`BLOCK_MUL` `variable`var, `family`array **DEPRECATED**\
Used to patch in multiple blocks at once. Use the `BLOCKM;` command to save multiple blocks to a variable, and use it here to patch-it in. Use the array input to specify the parent and child.\
`BLOCKM;` `opcodes`opcodes, `out`(c)var\
Use to save multiple blocks to a variable, example:
```bash
BLOCKM;
    var_set(MyVariable.v, "hello"),
    looks_say(MyVariable.v)
    TempBlocks.c
;
# the variable and look blocks would be saved to `TempBlocks.c`
```

### Advanced
`BLOCK_ADV` `variable`(c)var, `family`array **DEPRECATED**\
Used to edit every part of a block's metadata. Use the `BLOCK;` command to save a block to a variable, and use it here to patch-it in. Use the array input to specify the parent and child.\
`BLOCKADV;` `metadata`meta, `out`(c)var\
Used to specify the metadata of any block, example:
```bash
BLOCKADV;
    motion_goto #opcode
    {"XPOS": 0, "YPOS": 0} #inputs
    {} #fields
    false #shadow metadata
    false #toplevel
    [100,150] #position
    TempBlock.c
;
```

## Conditionals
### Simple Jumps
`JMP/JEZ/JGZ/JLZ/JNZ` `input`val, `label`label\
Jumps to a label if the input is equal, greater, less, or not zero, depending on the specific command *(`JMP` just jumps without condition)*. Simple and quick, there are better conditionals, but if you need something done quickly, then these should work.\
`JBL` `out`(c)var\
Jumps to the last jump, so if you jumped from the main script to a certain label, you can use `JBL` to jump back to before you last jumped. You can also use a variable to store your last jump, and use `JMP` to get back to that spot.
>**Tip:** Can be used to escape loops!

### Advanced
`IF` `condition`bool `;`\
A very common if condition, feed an input and if it's true, whatever code is inside will be executed, example:
```bash
OP_RAND 0, 1, if1_out.c
OP_EQUAL if1_out.c, 1, if1_out.c
# logs "works" if a random number happens to be 1
IF if1_out.c;
    LOG "works"
;
# you can also do else and if else
IF if1_out.c;
    LOG "works"
IF_ELSE if2_out.c;
    LOG "plan b?"
ELSE;
    LOG "uh, nope!"
;
```
`WHILE` `condition`bool `;`\
A while loop, make sure you update the input going into the while loop, otherwise it'll loop forever, example:
```bash
VAR_COMP while_index1.c, 0
OP_GREAT while_index1.c, 10, while_bool1.c

WHILE while_bool1.c;
    OP_JOIN "index ", while_index1.c, join_out.c
    LOG join_out.c
    # incraments while_index1.c by 1, and updates the bool
    OP_INC while_index1.c, 1
    OP_GREAT while_index1.c, 10, while_bool1.c
;
```
`FOR` `index`(c)var, `amount`val, `incrament`val`\
The incrament parameter is optional. A basic for loop, the index variable is automatically updated, example:
```bash
FOR for_index1.c, 10, 1;
    LOG for_index1.c
;
```
`SLEEP` `time`val\
Will wait a specified amount of time before continuing, this language isn't multithreaded, neither does it patch multiple things at the same time, so the only reason to use this is certain debugging or ensuring something is done before continuing.
>**Fun fact:** I had no idea where to put this, so here it is, in conditions! I'm not moving it either :)

## Operations
### single
`OP_` `NOT/LEN/ROUND/ABS/FLR/CEIL/SQRT/SIN/COS/TAN/ASIN/ACOS/ATAN/IN/LOG/E^/10^`,`out`(c)var\
Any operation with only a single input, most of these are just for numbers, except `NOT` and `LEN`, which are `boolean` and `any` respectively.

### double
`OP_` `SUM/SUB/MUL/DIV/RAND/GREAT/LESS/EQUAL/AND/OR/CONT/MOD`,`out`(c)var\
Any operation that has two inputs, most of these are just for numbers, except `SUM`, `SUB`, and `CONT`: While `CONT` is returns True or False if a string contains another string, `SUM` and `SUB` function as value and string operators, here are some examples to demonstrate:
```bash
OP_SUM 2, 2, op_out1.c
# returns 4
OP_SUM "hello", "world", op_out1.c
# returns "helloworld"

OP_SUB 5, 2, op_out1.c
# returns 3
OP_SUB 2, "helloworld", op_out1.c
# returns "e", functions the same as `char # of string`
```

## Files
### Imports
`FILE_IMP` `file`file, `type`str, `name`str\
Imports a file to that sprite's costumes, sounds, or list, specified via the `type` just have "cost", "sound", "list" as the argument to choose weather it's a costume, sound, or list. The asset you're importing has to already be in your mod/patch's folder, you can import assets into there via SCI.\
`FILE_REP` `file`file, `type`str, `replaced`str\
Same as `FILE_IMP`, except you can specify to replace an asset instead of adding a new one.

### Managing
#### files
`FILE_WRITE` `file`file, `data`any\
Overwrite the data of any file in your mod/patch's directory.\
`FILE_READ` `file`file, `out`(c)var\
Reads the data of any file in your mod/patch's directory.
`FILE_NEW` `address`file, `name`str, `data`any\
Creates a new file in your mod/patch's directory.\
`FILE_DEL` `file`file\
Deletes a file in your mod/patch's directory.
#### assets
`ASSET_WRITE` `asset`str, `metadata`meta, `data`any\
Overwrite the metadata of any asset in the project *(local)*.\
`ASSET_READ` `asset`str, `metadata`meta, `out`(c)var\
Reads the metadata of any asset in the project *(local)*.\
`ASSET_DEL` `asset`str\
Deletes any asset in the project *(local)*.
#### mods/patches
`REQUIRE` `id`val\
Adds any shared comp variables and/or assets from the required mod/patch.\
`COMP_RETURN` `comp variable`cvar\
`FILE_RETURN` `file`file, `allowWrite?`bool\
`ASSET_RETURN` `name`str `type`str\
Shares comp variables and assets to any mod/patch that requires *your* mod/patch.

## Extension
`IMPORT` `name`str, `url`url\
Allows you to import an extension, where you can use `BLOCKADV;` to use it's blocks. There are many ways you can call this command, here are examples of all of them:
```js
//default, just uses a URL for the js
IMPORT JSON, https://extensions.turbowarp.org/Skyhigh173/json.js
//uses a file as the js instead
IMPORT JSON, M:/extensions/JSON.js
//just has the raw DATAurl data
IMPORT JSON, M:/extensions/JSON.txt
```
```bash
BLOCKADV;
    JSON_json_is_valid #opcode
    "json":[1,[10,""]] #inputs
    {} #fields
    false #shadow metadata
    true #toplevel
    [-20,1110] #position
    TempBlock.c
;
```
