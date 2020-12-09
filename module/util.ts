import { debug as debugInit } from "./deps.ts";
import { Month } from "./types.ts";

// Our exported debug module created once to speed up startup time.
export const debug = debugInit("aoc");

export const readJSON = (path: string) => {
  try {
    return JSON.parse(Deno.readTextFileSync(path));
  } catch (error) {
    return {};
  }
};

const evalTemplateLiteral = (
  template: string,
  templateVariables: unknown,
) => {
  const templateVariableRegex = /(\${)([a-z]+})/g;
  template = template.replaceAll(templateVariableRegex, "$1this.$2");
  const evaluatedTemplate: string = new Function(`return \`${template}\`;`)
    .call(
      templateVariables,
    );
  return evaluatedTemplate;
};

export const getDayFilePath = (day: number, template: string) => {
  const num = String(day).padStart(2, "0");
  const dayPath = evalTemplateLiteral(template, {
    num,
  });
  return dayPath;
};

export const checkIfValidAOCDay = (day: number) => {
  if (typeof day !== "number" || day < 1 || day > 25) {
    throw new RangeError(
      "The day must be a number in the range 1 to 25 inclusive.",
    );
  }
};

export const checkIfValidAOCYear = (year: number) => {
  const now = new Date();
  const latestAOCYear =
    (now.getMonth() === Month.DECEMBER
      ? now.getFullYear()
      : now.getFullYear() - 1);
  if (year < 2015 || year > latestAOCYear) {
    throw new RangeError(
      "The year must be a valid AOC year.",
    );
  }
};

export const parsePart = (part: string) => {
  part = part.replace(/^[^\d]*/, "");
  const partNumber = Number.parseInt(part, 10);
  if (!(partNumber === 1 || partNumber === 2)) {
    throw new RangeError("part must be 1 or 2");
  }

  return partNumber;
};

export const isURL = (string: string) => {
  try {
    const url = new URL(string);
    return true;
  } catch (error) {
    return false;
  }
};
