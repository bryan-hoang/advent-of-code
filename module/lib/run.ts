import fetchInput from "./tools/fetch_input.ts";
import { debug } from "../util.ts";
import type { AdventOfCodeConfig } from "../types.ts";

const run = async (config: AdventOfCodeConfig) => {
//   let input = await getInput(config);
//   debug(`Getting day module at ${config.dayFilepath}`);
//   const dayModule = await import(config.dayFilepath);
//   const options = Object.assign(
//     {
//       noTrim: false,
//     },
//     dayModule.options,
//   );

//   if (!options.noTrim) {
//     input = input.trim();
//   }

//   let output;
//   if (config.part === 1) {
//     debug(`Running part 1`);
//     output = dayModule.part1(input);
//   } else if (config.part === 2) {
//     debug(`Running part 2`);
//     output = dayModule.part2(input);
//   } else {
//     throw new RangeError("Not a valid part. Must be 1 or 2.");
//   }
//   return output;
};

export default run;
