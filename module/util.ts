import { debug as debugInit } from "./deps.ts";
import { Month } from "./types.ts";

// Our exported debug module created once to speed up startup time.
export const debug = debugInit("advent");

export const readJSON = (path: string) => {
  try {
    return JSON.parse(Deno.readTextFileSync(path));
  } catch (error) {
    return {};
  }
};

export const getDayPath = (day: number, template: string) => {
  // Create the day filename
  // Make it always two length with leading 0
  const stringDay = String(day).padStart(2, "0");
  return template.replace("{{num}}", stringDay);
};

export const isValidAOCDay = (day: number) => {
  return day < 1 || day > 25;
};

export const isValidAOCYear = (year: number) => {
  const now = new Date();
  const latestAOCYear = (now.getMonth() === Month.DECEMBER
  ? now.getFullYear()
  : now.getFullYear() - 1);
  return year < 2015 || year > latestAOCYear;
};
