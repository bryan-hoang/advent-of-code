import { assert } from "../dev_deps.ts";
import run from "./run.ts";

Deno.test({
  name: "run",
  fn: () => {
    assert(true);
  },
});
