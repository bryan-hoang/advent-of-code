import { assert } from "../dev_deps.ts";
import { RunOptions } from "../types.ts";
import run from "./run.ts";

Deno.test({
  name: "run",
  fn: async () => {
    const day = 1;
    const part = 1;
    const inputFlag = undefined;
    const options: RunOptions = {
      year: 2020,
      nameTemplate: "examples/day_${num}.ts",
      inputFile: "examples/input.txt",
    };
    await run(day, part, inputFlag, options);
  },
});
