import fetchInput from "./tools/fetch_input.ts";
import { debug, getDayFilePath } from "../util.ts";
import type { DayModule, RunOptions } from "../types.ts";
import getConfig from "./tools/get_config.ts";
import { existsSync, path } from "../deps.ts";

const run = async (
  day: number,
  part: 1 | 2,
  inputFlag: "-" | undefined,
  options: RunOptions,
) => {
  const aocConfig = getConfig();
  const nameTemplate = options.nameTemplate || aocConfig.nameTemplate;
  const year = options.year || aocConfig.year;
  const inputFile = options.inputFile || aocConfig.inputFile;
  const dayFile = getDayFilePath(day, nameTemplate);

  const input = await getInput(inputFlag, inputFile, year, day);
  const { part1, part2 } = await getParts(dayFile);

  console.log(`Running day ${day} part ${part}...`);
  let answer: string;
  switch (part) {
    case 1:
      answer = part1(input);
      break;
    case 2:
      answer = part2(input);
      break;
    default:
      // Shouldn't get to this point due to earlier type checking.
      throw new RangeError("Invalid part specified");
  }

  // If the part functions simply returned the inputs
  if (String(answer).indexOf("\n") !== -1) {
    console.log("Answer is multiple lines long. Printing only the first line:");
    console.log(answer.split("\n")[0]);
  } else {
    console.log("Answer:", answer);
  }
};

async function getInput(
  inputFlag: string | undefined,
  inputFile: string,
  year: number,
  day: number,
) {
  let input: string;
  if (inputFlag === "-") {
    debug("Reading input from stdin");
    const { stdin, readAllSync } = Deno;
    const inputData = readAllSync(stdin);
    const decoder = new TextDecoder();
    input = decoder.decode(inputData);
  } else if (existsSync(inputFile)) {
    debug(`Reading input from ${inputFile}`);
    input = Deno.readTextFileSync(inputFile);
  } else {
    debug(
      `Input file not found, reading input from https://adventofcode.com/${year}/day/${day}/input`,
    );

    input = await fetchInput({ year, day });
    debug("Reading input from stdin");
  }

  debug("Finished reading input");
  return input;
}

async function getParts(dayFile: string) {
  if (
    existsSync(dayFile) && !dayFile.endsWith(".js") && !dayFile.endsWith(".ts")
  ) {
    throw new Error(`Cannot find module to import from ${dayFile}`);
  }

  const dayFileImportPath = `file:/${path.resolve(dayFile)}`;
  debug(`Dynamically importing ${dayFileImportPath}`);
  const dayModule: DayModule = await import(dayFileImportPath);
  debug("Imported day module:", dayModule);
  const { part1, part2 } = dayModule;
  if (typeof part1 !== "function" || typeof part2 !== "function") {
    throw new Error(
      `Module imported from ${dayFile} is not exporting part1 and part2 functions`,
    );
  }

  debug("part1:", part1);
  debug("part2:", part2);

  return { part1, part2 };
}

export default run;
