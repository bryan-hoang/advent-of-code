import advent from "./lib/aoc_api.ts";
import debug from "./util/debug.ts";

import type { Config } from "./types.ts";

const getInput = (
  input: string,
  config: { year: number; day: number; session: string },
) => {
  let inputPromise;
  if (input === "+") {
    // If input is `+`, get from adventofcode
    const cacheKey = `${config.year}:${config.day}`;
    debug(`Input is from adventofcode.com. Checking cache.`);

    debug("Cache not found. Retrieving from adventofcode.com.");
    inputPromise = advent
      .getInput({
        year: config.year,
        day: config.day,
        session: config.session,
      });
  } else {
    // Otherwise, just use raw input value
    debug("Getting raw input from argument");
    inputPromise = Promise.resolve(input);
  }
  return inputPromise.then((input: string) => {
    debug("Successfully got input");
    return input;
  });
};

const run = async (rawInput: string, config: Config) => {
  let time;
  let input = await getInput(rawInput, config);
  debug(`Getting day module at ${config.dayFilepath}`);
  const dayModule = await import(config.dayFilepath);
  const options = Object.assign(
    {
      noTrim: false,
    },
    dayModule.options,
  );

  if (!options.noTrim) {
    input = input.trim();
  }

  let output;
  if (config.part === 1) {
    debug(`Running part 1`);
    output = dayModule.part1(input);
  } else if (config.part === 2) {
    debug(`Running part 2`);
    output = dayModule.part2(input);
  } else {
    throw new RangeError("Not a valid part. Must be 1 or 2.");
  }
  return output;
};

export default run;
