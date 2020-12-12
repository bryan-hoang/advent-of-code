# advent_of_code

![Deno](https://github.com/bryan-hoang/advent-of-code/workflows/Deno/badge.svg)
[![vr scripts](https://badges.velociraptor.run/flat.svg)](https://velociraptor.run)
[![GitHub stars](https://img.shields.io/github/stars/bryan-hoang/advent-of-code)](https://github.com/bryan-hoang/advent-of-code/stargazers)
[![GitHub license](https://img.shields.io/github/license/bryan-hoang/advent-of-code)](https://github.com/bryan-hoang/advent-of-code/blob/main/LICENSE)
[![GitHub forks](https://img.shields.io/github/forks/bryan-hoang/advent-of-code)](https://github.com/bryan-hoang/advent-of-code/network)
[![GitHub issues](https://img.shields.io/github/issues/bryan-hoang/advent-of-code)](https://github.com/bryan-hoang/advent-of-code/issues)

---

A CLI tool help initialize and run Typescript/JavaScript files to solve
advent-of-code challenges written for Deno. It was heavily inspired by
[@ksmithut](https://github.com/ksmithut)'s
[advent-of-code](https://www.npmjs.com/package/advent-of-code) npm package.

## Installation

```shell
deno install --unstable --allow-env --allow-read --allow-write --allow-net -f -n aoc https://deno.land/x/advent_of_code/cli.ts
```

## Usage

```shell
# Create a day file from a template file and get the input file
aoc init <day>

# Example:
aoc init 1

# Runs a day file based on the given arguments. Can pipe the input into
# the command with `-` instead of having it read the input file.
aoc run <day> <part> [input]

# Example
aoc run 1 1 - < input.txt

# Get description of other options.
aoc -h
```

## Configuration

`aoc` can be configured using a json file called `advent_of_code.json`. If you
pass in command-line arguments, they will override your `advent_of_code.json`
configuration.

### JSON config (`advent_of_code.json` template)

aoc configuration can be provided as a JSON file:

```json
{
  // Optional but highly recommended
  "$schema": "https://deno.land/x/advent_of_code/schema.json",

  "year": 2020,
  "nameTemplate": "day_${num}.ts",
  "templateFile": "https://deno.land/x/advent_of_code/templates/day.ts",
  "inputFile": "input.txt"
}
```

<!-- To create a basic configuration in the root directory of your project file you
can run:

```shell
aoc --init
```

this will create a basic `advent_of_code.json` file:

```json
{
  "year": 2020,
  "nameTemplate": "day_${num}.ts",
  "templateFile": "https://deno.land/x/advent_of_code/templates/day.ts"
}
``` -->

## Debugging

`aoc` leverages the [debug](https://deno.land/x/debug) module. Setting
`DEBUG=aoc` will print out debug information. When reporting bugs, please have
the output from this handy so that the issue can be determined more quickly.

## Disclaimer

I am not affiliated with [adventofcode.com](https://adventofcode.com) or any of
their sponsors, employees, pets, or anything relating to them. I am an active
participant, and I wanted to make a tool to make it easier to setup and run
advent of code things. Please don't abuse
[adventofcode.com](https://adventofcode.com). This tool could be used to make a
lot of automated requests to their
site<!-- , which is why this tool leverages caching -->. If you find that you're
making too many requests to [adventofcode.com](https://adventofcode.com) because
of this module, please let me know so I can resolve any issues. If this module
is used to abuse [adventofcode.com](https://adventofcode.com), I will unpublish
it from deno.land and remove this code from github.

## TODO

Summary of progress tracking for the
[project](https://github.com/bryan-hoang/advent-of-code/projects/1):

- [ ] Improve test suite
- [ ] Flush out examples
- [ ] Implement `aoc --init`: Initialize a default config file.
- [ ] Implement `aoc submit`: Submit answers to Advent of Code puzzles.
- [ ] Create programmatic API (similar to
      [advent-of-code-client](https://www.npmjs.com/package/advent-of-code-client))
      the mirrors the CLI functions (e.g. get input, run, submit). This would
      make the project not be a pure cli tool anymore.
- [ ] Add proper caching. Instead of relying on the file existing. I would like
      to use the [Deno cache library](https://deno.land/x/cache), but it's still
      very new and doesn't support modifying the headers when fetching the
      files.

## Contributing

Refer to [CONTRIBUTING.md](./CONTRIBUTING.md): Please follow the
[Code of Conduct](./CODE_OF_CONDUCT.md). Pull request, issues and feedback are
very welcome. Code style is formatted with `deno fmt` and commit messages are
done following [Conventional Commits](https://www.conventionalcommits.org) spec.

## License

Copyright (c) 2020-present Bryan Hoang. All rights reserved. MIT license.
