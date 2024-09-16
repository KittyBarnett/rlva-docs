[DRAFT]

An RLV command follows a specific syntax, which can be broken down into three main parts:

`@<behaviour>[:<option>]=<type>`

- `behaviour` and `type` are always required regardless of the specific command.
- `option` depends on the specific command being executed (and could be optional).

Multiple commands can be chained using the `,` separator. This is generally encouraged, especially for any 'force commands' that affect the avatar's appearance.

#### Behaviour

The behaviour defines what you want to influence.

#### Option

The option is context-dependent on the behaviour that precedes it. Refer to a command's documentation for specifics.

#### Command types

There are three main forms of RLV commands:

1. **Restrictions** (aka add/remove commands)
2. **Actions** (aka force commands)
3. **Queries** (aka reply commands)

### Example of a Command

A command is a combination of a behaviour and a type. For instance, the behaviour `remoutfit` can be used as both a restriction (preventing the avatar from taking off clothing layers) or as an action (taking off all of an avatar's clothing layers).

### Restrictions

Restrictions generally prevent an avatar from doing something they would normally be able to do. They are ongoing effects that last until explicitly removed. An example of a restriction is preventing teleportation via the world map.

Restrictions can be added using the `=n` or `=add` syntax and removed using `=y` or `=rem`. These are interchangeable.

#### Examples:

- `@detach=n` and `@detach=add` are synonyms.
- `@remoutfit=n,remoutfit=rem` first sets the `remoutfit` behaviour and then immediately removes it again.

While scripts are used to set and unset restrictions, the restriction itself is associated with the object the script is in. If a linkset contains two objects, each with its own script, both can independently add or remove the same restriction without affecting the other. However, two scripts in the same object will share restrictions and may undo each other's restrictions.

Scripts can only affect behaviours held by the object they are in and cannot undo a restriction set by another object.

### Actions

Actions are one-time commands that affect the avatar or their viewer in some way (e.g., force-sitting an avatar onto a specific object).

### Queries

Queries are commands used by scripts to retrieve information from RLV (e.g., to enumerate over `#RLV` shared inventory folders).
