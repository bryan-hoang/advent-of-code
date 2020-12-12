import { ensureFileSync, existsSync } from "../deps.ts";
import { debug, getDayFilePath, isURL } from "../util.ts";
import type { InitOptions } from "../types.ts";
import fetchInput from "./tools/fetch_input.ts";
import getConfig from "./tools/get_config.ts";

/**
 * Initializes the day file and input to run if the day and input don't already exist already exist.
 * @param {InitConfig} config
 */
async function init(
  day: number,
  options: InitOptions,
) {
  const aocConfig = getConfig();
  const nameTemplate = options.nameTemplate || aocConfig.nameTemplate;
  const templateFile = options.templateFile || aocConfig.templateFile;
  const year = options.year || aocConfig.year;
  const inputFile = options.inputFile || aocConfig.inputFile;
  const force = options.force;
  const dayFile = getDayFilePath(day, nameTemplate);

  await ensureDayFileExists({
    dayFile,
    templateFile,
    force,
  });

  await ensureInputFileExists({
    year,
    day,
    inputFile,
    force,
  });
}

async function ensureDayFileExists(
  { dayFile, templateFile: dayFileTemplate, force }: {
    dayFile: string;
    templateFile: string;
    force?: boolean;
  },
) {
  debug(`Checking for existing file: ${dayFile}`);
  const doesDayFileExist = existsSync(dayFile);
  if (doesDayFileExist) {
    if (force) {
      console.log(`${dayFile} found, forcing creation`);
    } else {
      console.log(`${dayFile} found, skipping creation`);
      return;
    }
  } else {
    console.log(`${dayFile} not found, proceeding with creation`);
  }

  console.log(`Generating ${dayFile} from ${dayFileTemplate}`);
  let templateFileData;
  if (isURL(dayFileTemplate)) {
    const templateFileURL = new URL(dayFileTemplate);
    const response = await fetch(templateFileURL);
    debug("%O", response);
    if (!response.ok) {
      throw new Error(`Unable to fetch template file from ${dayFileTemplate}`);
    }

    templateFileData = new Uint8Array(await response.arrayBuffer());
  } else {
    templateFileData = Deno.readFileSync(dayFileTemplate);
  }

  ensureFileSync(dayFile);
  Deno.writeFileSync(dayFile, templateFileData);
}

async function ensureInputFileExists({ inputFile, year, day, force }: {
  inputFile: string;
  year: number;
  day: number;
  force?: boolean;
}) {
  const doesInputFileExist = existsSync(inputFile);
  if (doesInputFileExist) {
    if (force) {
      console.log(`${inputFile} found, forcing creation`);
    } else {
      console.log(`${inputFile} found, skipping creation`);
      return;
    }
  } else {
    console.log(`${inputFile} not found, proceeding with creation`);
  }

  console.log(
    `Fetching input file from https://adventofcode.com/${year}/day/${day}/input`,
  );
  const input = await fetchInput({ year, day });
  const encoder = new TextEncoder();
  ensureFileSync(inputFile);
  const inputFileData = encoder.encode(input);
  Deno.writeFileSync(inputFile, inputFileData, { create: false });
}
export default init;
