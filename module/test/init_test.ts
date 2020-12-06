import { assert } from "../test_deps.ts";
import { debug } from "../util.ts";
import init from "../init.ts";
import { path } from "../deps.ts";

Deno.test({
  name: "init",
  fn: () => {
    const success = init(
      { dayFilePath: "test/tmp/day_1.ts", templateFile: "template/day.ts" },
    );
    assert(success);
  },
});
