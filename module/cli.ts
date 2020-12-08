import { Command, HelpCommand, path } from "./deps.ts";
import {
  checkIfValidAOCDay,
  checkIfValidAOCYear,
  debug,
  getDayPath,
  readJSON,
} from "./util.ts";
import init from "./lib/init.ts";
// import run from "./run.ts";
import { version } from "./version.ts";
import { AdventOfCodeConfig, InitOptions, Month } from "./types.ts";

const main = () => {
  const initCommand = new Command()
    .arguments("<day:number>")
    .description("Initializes the file and input for a given day")
    .option(
      "-y, --year <year:number>",
      "Select the advent year you are running",
      {
        value: (year: number): number => {
          checkIfValidAOCYear(year);
          return year;
        },
      },
    )
    .option(
      "-t, --template-file <filepath:string>",
      "The path to a template file",
    )
    .option(
      "-n, --name-template <filepathtemplate:string>",
      "The filename template to use when looking for day files",
    )
    .option(
      "-i, --input-file <filenamepath:string>",
      "The name of the input file to create after downloading it",
    )
    .option(
      "-f, --force [force:boolean]",
      "Will override an existing file",
    )
    .action((options: InitOptions, day: number) => {
      debug("init args:", day);
      debug("init options:", options);
      checkIfValidAOCDay(day);
      init(day, options);
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
