import { assert } from "../../../dev_deps.ts";
import { getInput } from "../../../lib/tools/aoc_api.ts";

Deno.test({
  name: "getInput returns the input as a string",
  fn: async () => {
    const input = await getInput(
      { year: 2015, day: 1 },
    );
    assert(typeof input === "string");
  },
});
