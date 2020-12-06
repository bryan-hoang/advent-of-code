import { existsSync } from "./deps.ts";
import { debug } from "./util.ts";
import type { InitConfig } from "./types.ts";

/**
 * Initializes the template file to run if the day file doesn't already exist.
 * @param {InitConfig} config
 */
const init = (
  { dayFilePath, templateFile, force }: InitConfig,
) => {
  debug(`Checking for existing file: ${dayFilePath}`);
  const doesDayFileExist = existsSync(dayFilePath);
  if (doesDayFileExist) {
    debug("Found existing file");
    if (force) {
      debug("Forcing creation of file");
    } else {
      debug("Skipping creation of file");
      return;
    }
  }

  debug(`Generating ${dayFilePath} from ${templateFile}`);
  const templateFileData = Deno.readFileSync(templateFile);
  Deno.writeFileSync(dayFilePath, templateFileData);
  debug(`Generated ${dayFilePath} successfully`);
  return true;
};

export default init;
