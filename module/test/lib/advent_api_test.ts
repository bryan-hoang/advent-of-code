import { assert } from "../../test_deps.ts";
import { config } from "../../deps.ts";
import { getInput } from "../../lib/aoc_api.ts";
import { debug } from "../../util.ts";

const env = config();

debug("env:", env);

Deno.test({
  name: "getInput returns the input as a string",
  fn: async () => {
    const input = await getInput(
      { year: 2015, day: 1, session: env.ADVENT_SESSION },
    );
    assert(typeof input === "string");
  },
});
