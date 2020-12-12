import { Command, HelpCommand } from "./deps.ts";
import { checkIfValidAOCDay, checkIfValidAOCYear, debug } from "./util.ts";
import init from "./lib/init.ts";
import run from "./lib/run.ts";
import { version } from "./version.ts";
import { CommandOptionsArgs, InitOptions, RunOptions } from "./types.ts";

const main = () => {
  const yearCommandOptionArgs: [string, string, {
    value: (value: number) => number;
  }] = [
    "-y, --year <year:number>",
    "Select the advent year you are running.",
    {
      value: (year: number): number => {
        checkIfValidAOCYear(year);
        return year;
      },
    },
  ];

  const nameTemplateCommandOptionsArgs: CommandOptionsArgs = [
    "-n, --name-template <filepathtemplate:string>",
    "The filename template to use when looking for day files. Has to contain ${num} to substitute for the day number.",
  ];

  const initCommand = new Command()
    .arguments("<day:number>")
    .description("Initializes the file and input for a given day.")
    .option(...yearCommandOptionArgs)
    .option(
      "-t, --template-file <filepath:string>",
      "The path to a template file.",
    )
    .option(...nameTemplateCommandOptionsArgs)
    .option(
      "-i, --input-file <filepath:string>",
      "The name of the input file to create after downloading it.",
    )
    .option(
      "-f, --force [force:boolean]",
      "Will override an existing file.",
    )
    .action(async (options: InitOptions, day: number) => {
      debug("init args:", day);
      debug("init options:", options);
      checkIfValidAOCDay(day);
      await init(day, options);
    });

  const runCommand = new Command()
    .arguments("<day:number> <part:number> [input:string]")
    .description(
      "Runs a given day and part. Can give the input directly through stdin (specify with -), else it will try to find and read the input file before fetching the input from the website.",
    )
    .option(...yearCommandOptionArgs)
    .option(...nameTemplateCommandOptionsArgs)
    .option(
      "-i, --input-file <filepath:string>",
      "The name of the input file to look for.",
    )
    .action(async (options: RunOptions, ...args: [number, number, "-"?]) => {
      debug("run args:", args);
      const [day, part, inputFlag] = args;
      debug("run options:", options);
      if (part !== 1 && part !== 2) {
        throw new RangeError("The part must be 1 or 2.");
      }
      checkIfValidAOCDay(day);
      await run(day, part, inputFlag, options);
    });

  const aoc = new Command();
  aoc
    .name("aoc")
    // Show help by default
    .action(function () {
      this.help();
    })
    .command("help", new HelpCommand().global())
    .version(version)
    .command("init", initCommand)
    .command("run", runCommand)
    .parse(Deno.args);

  /**
   * advent run <input>
   */
  // program
  //   .command("run <day> <part> [input]")
  //   .description("Runs a given day with the given input")
  //   .option(
  //     "-y, --year [year]",
  //     "Select the advent year you are running",
  //     Defaults.year,
  //   )
  //   .option(
  //     "-n, --name-template [dayFileNameTemplate]",
  //     "The filename template to use when looking for day files",
  //     Defaults.dayFileNameTemplate,
  //   )
  //   .option("-s, --session [session]", "Session cookie to make requests");
  // .action((day: string, part: string, input: string, command: AdventOfCodeConfig) => {
  //   const config = getConfig(day, command);
  //   config.part = parsePart(part);
  //   debug('Running "run" with following config: %O', config);
  //   action = run(input, config);
  // });

  // program.command("help", "Print help info");
};

if (import.meta.main) {
  main();
}
