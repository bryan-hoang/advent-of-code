import { assert } from "../../dev_deps.ts";
import fetchInput from "./fetch_input.ts";

Deno.test({
  name: "getInput returns the input as a string",
  fn: async () => {
    const input = await fetchInput(
      { year: 2015, day: 1 },
    );
    assert(typeof input === "string");
  },
});
