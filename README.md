# Scratch Code Injector
## What is SCI?
SCI is a tool for patching, and modding Scratch projects. It lets you install, manage, and even create your own mods for any [compatible](#how-are-projects-supported)[^3] Scratch project. Then, whenever you want, SCI will automatically patch and export the project, all from the press of a button. Though it's major use is for modding, it can also be used for editing projects outside of the Scratch editor, collaborating, and more.

## How do I use SCI?
### Modding projects
Before you can do anything with mods, you'll have to get its source code, or a SCI-related file for the project, like an `.mpj`[^1]. Now this is typically pretty easy, if the project is featured on SCI, you can start from there, but for packaged projects where the source code isn't accessible, you'll have to hope the project [supports](#how-are-projects-supported) modding with SCI. Unsupported projects, with public access to source code, are still moddable, so it's recommended you check in with a creator, unless it's stated somewhere that you're allowed to modify their project. But if the project [supports](#how-are-projects-supported) SCI, then that should indicate that you're allowed to mod it.

Once you have the proper `.json` or `.mpj`[^1] file loaded into SCI, you'll be able to see certain things about the project on its page, like how many mods people have made for it, it's current version, and more, though some of this data will only appear if the project has an `SCID`[^2]. Here you'll be able to install any mods, create your own, and then patch the project and export it. Then, depending on the support of the project, it should be as easy as entering the project, and finding a button that lets you import your file containing the modded and patched game, from there, the game should automatically update. If the game doesn't support SCI, you'll have to turn the game's `.sb3` into a zip file, extract it, replace the `project.json` file, and then zip it back up and make it a `.sb3` file.

### Using SCI's interface
SCI has a lot of menus and buttons, so it can be confusing where to find certain things, so here you'll be able to find where anything is...

## How are projects supported?
### What does having support mean?
🟢 **supported**:
	- A project where the creator has officially integrated SCI, presumably for easy-modding.\
🟡 **compatible, yet unsupported**:
	- A project that should be moddable, but not officially, simply via access to the game's source code.\
🔴 **blacklisted/incompatible**:
	- A project that can't be modded entirely.

### How to modify, and add support as a creator
#### Adding support
If you want your game (or project in general) to have an `SCID` and/or have easy modding support, head over to SCI, and go to `Games > New Game`. There you'll be able to import your game, where you can generate an `SCID`, make a page for your game, and get the `SCIsupport.sprite3` sprite, where you'll be able to customize how SCI will interact with your game, and all will be integrated into your project automatically.

#### Editing the project's page
As long as you're in the same account you submitted the game with, you'll be able to edit the game's page via `Games > My Games > [game name]`. There you can edit data, add cover art, and more.

#### Updating your game
If your game gets an update, you'll obviously want to update the game's page too, just head over to your game's page via `Games > My Games > [game name]`, and then find the `update` button, you'll be able to specify the new version of the game, and provide a new `project.json` if you chose for your game's page to also have a vanilla download of your game.

#### Blacklisting your game
If you don't want your game to be modded via SCI, head over to `Games>New Game` and check the [blacklist] button, so instead of creating a page and all that, instead it'll give your project an `SCID`, and add your game to a database, so it can't modded or patched with SCI.

#### `SCID`s
`SCID`s are IDs for your project, they work similarly to how advanced settings work on turbowarp, they functionally store your project's metadata in the project itself. Though unlike advanced settings, they're not stored as a fragile note, that could easily be deleted. Instead it's stored in your project. A project without an `SCID` will have a harder time with modding, than one with an `SCID`, since it gives access for versions, and certain, unrelated compatibility features.

[^1]: `.mpj` files are a file type built for SCI, they work the same way as the typical `.json` file that you'd normally use, except `.mpj` files are encoded and make project data less immediately accessible, than with a normal `.json` file.
[^2]: and `SCID` is an ID and metadata for projects that want to have SCI data attached to them, they basically contain a project's version, name, compatibility, and more. It is stored in the project itself, and is easily readable, meaning other tools, not just SCI, can use the `SCID`. You can setup an `SCID` for your project via SCI, learn more about `SCID`s [here](#how-to-modify-and-add-support-as-a-creator).
[^3]: supported, official, and compatible are all words thrown around. Supported means a project officially supports SCI, so it has the `SCIsupport.sprite3` sprite in it, compatible means if SCI can even mod a project, a non-compatible project would typically be a project without accessible source code, or one that's blacklisted.
