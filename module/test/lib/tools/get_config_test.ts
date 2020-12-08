import { assert } from "../../../dev_deps.ts";
import { debug } from "../../../util.ts";
import getConfig from "../../../lib/tools/get_config.ts";

Deno.test({
  name: "getConfig",
  fn: () => {
    const aocConfig = getConfig();
    debug("Final config:", aocConfig);
    assert(aocConfig);
  },
});
