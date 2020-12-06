import { Command, path } from "./deps.ts";
import { debug, isValidAOCDay, readJSON, getDayPath } from "./util.ts";
import init from "./init.ts";
import { version } from "./mod.ts";
import run from "./run.ts";
import type { Config, InitConfig } from "./types.ts";

const defaultTemplateFile = path.resolve(Deno.cwd(), "templates", "day.js");
const defaultNameTemplate = "day_{{num}}.ts";

const parseDay = (dayString: string) => {
  dayString = dayString.replace(/^[^\d]*/, "");
  const dayNumber = Number(dayString);
  if (!isValidAOCDay(dayNumber)) {
    throw new RangeError("Day must be between 1 and 25 inclusive");
  }

  return dayNumber;
};

const parsePart = (part: string) => {
  part = part.replace(/^[^\d]*/, "");
  const partNumber = Number.parseInt(part, 10);
  if (!(partNumber === 1 || partNumber === 2)) {
    throw new RangeError("part must be 1 or 2");
  }

  return partNumber;
};

const logUsage = () => {
  console.log("");
  console.log("Examples:");
  console.log("");
  console.log("    advent run --day 1 --part 1 'this is my input'");
  console.log("    cat input.txt | advent run -d 1 -p 1 -");
  console.log("    advent run -d 1 -p 1 - < input.txt");
  console.log("    advent run -d 1 -p 1 + --session 'session=asefsafes...'");
  console.log("");
  console.log("Notes:");
  console.log("");
  console.log(
    "    For anything that reaches out to advent-of-code.com, you need to",
  );
  console.log(
    "    provide your session token. You can get this by opening up the",
  );
  console.log(
    "    network tab in the devtools, logging into to adventofcode.com, then",
  );
  console.log("    viewing what gets sent as the `Cookie:` request header on");
  console.log(
    "    subsequent requests. You may pass in the required value using",
  );
  console.log(
    "    `--session [value]` or using the `ADVENT_SESSION` environment",
  );
  console.log("    variable. Note that it likely starts with `session=`");
};

const cli = () => {
  // Reading the config.
  const adventConfigPath = path.resolve("advent.json");
  const adventConfig = readJSON(adventConfigPath);
  const now = new Date();
  const defaultYear = adventConfig.year ||
    (now.getMonth() === Month.DECEMBER
      ? now.getFullYear()
      : now.getFullYear() - 1);
  const nameTemplate = adventConfig.nameTemplate || defaultNameTemplate;
  const templateFile = adventConfig.templateFile
    ? path.resolve(adventConfig.templateFile)
    : defaultTemplateFile;

  const getConfig = (day: string, args: Config) => {
    const config: Config = {
      year: args.year || (new Date()).getFullYear(),
      session: args.session || Deno.env.get("ADVENT_SESSION") || "",
      day: parseDay(day),
      nameTemplate: args.nameTemplate,
      templateFile: args.templateFile,
      dayFilepath: "",
    };
    const dayFilename = getDayPath(config.day, config.nameTemplate);
    config.dayFilepath = path.resolve(dayFilename);
    return config;
  };

  const program = new Command("advent");
  program.version(version);
  program.on("--help", logUsage);
  let action;

  /**
   * advent run <input>
   */
  program
    .command("run <day> <part> <input>")
    .description("Runs a given day with the given input")
    .option(
      "-y, --year",
      "Select the advent year you are running",
      defaultYear,
    )
    .option("-s, --session [session]", "Session cookie to make requests")
    .option(
      "-n, --name-template [template]",
      "The filename template to use when looking for day files",
      defaultNameTemplate,
    )
    .action((day: string, part: string, input: string, command: Config) => {
      const config = getConfig(day, command);
      config.part = parsePart(part);
      debug('Running "run" with following config: %O', config);
      action = run(input, config);
    });

  /**
   * advent init
   */
  program
    .command("init <day>")
    .description("Initializes the file for a given day")
    .option(
      "-n, --name-template [template]",
      "The filename template to use when looking for day files",
      defaultNameTemplate,
    )
    .option(
      "-t, --template-file [filepath]",
      "The path to a template file",
      defaultTemplateFile,
    )
    .option("-f, --force", "Will override an existing file", false)
    .action((day: string, command: InitConfig) => {
      const config = getConfig(day, command);
      config.force = command.force;
      debug('Running "init" with following config: %O', config);
      action = init(config);
    });

  program.parse(Deno.args);

  if (!action) {
    return program.help();
  }

  return action;
};

if (import.meta.main) {
  cli();
}
