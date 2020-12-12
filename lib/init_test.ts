import { Defaults } from "../lib/constants.ts";
import init from "../lib/init.ts";

Deno.test({
  name: "init",
  fn: async () => {
    const day = 1;
    const commonInitConfig = {
      templateFile: "templates/day.ts",
      inputFile: "tmp/input.txt",
      nameTemplate: "tmp/day_${num}.ts",
    };

    await init(day, {
      ...commonInitConfig,
      force: true,
    });

    await init(day, {
      ...commonInitConfig,
      force: false,
    });

    await init(day, {
      ...commonInitConfig,
      force: true,
      templateFile: Defaults.templateFile,
    });
  },
});
