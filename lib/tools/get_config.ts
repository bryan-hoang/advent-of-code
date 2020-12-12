import { path } from "../../deps.ts";
import { debug, readJSON } from "../../util.ts";
import { AdventOfCodeConfig } from "../../types.ts";
import { Defaults } from "../constants.ts";

/**
 * Reads the config stored in the given path and returns a config object with
 * all values filled in.
 */
const getConfig = (configPath = "advent_of_code.json") => {
  // Reading the config.
  const aocConfigPath = path.resolve(configPath);
  debug("aocConfigPath:", aocConfigPath);
  const aocConfig: AdventOfCodeConfig = readJSON(aocConfigPath);
  debug("Read config:", aocConfig);

  // Set default properties
  const year = Number(aocConfig.year) || Defaults.year;
  const templateFile = aocConfig.templateFile ||
    Defaults.templateFile;
  const nameTemplate = aocConfig.nameTemplate ||
    Defaults.nameTemplate;
  const inputFile = aocConfig.inputFile || Defaults.inputFile;

  const config = {
    year,
    templateFile,
    nameTemplate,
    inputFile,
  };

  debug("Final config:", config);

  return config;
};

export default getConfig;
