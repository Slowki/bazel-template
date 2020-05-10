# Bazel Template
A quick start template for Bazel projects.

## Formatting
`bazel run //tools:format`

## Update `compile_commands.json`
`bazel run //tools:compile-commands`

## Install the Git Hooks
```sh
cd .git
rm -r hooks
ln -s ../tools/hooks
```

## Build the `hello_world` Target
`bazel build //hello_world`
