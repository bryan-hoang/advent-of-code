import { Month } from "../types.ts";

const now = new Date();

export const Defaults = {
  year:
    (now.getMonth() === Month.DECEMBER
      ? now.getFullYear()
      : now.getFullYear() - 1),
  templateFile: "https://deno.land/x/advent_of_code/templates/day.ts",
  nameTemplate: "day_${num}.ts",
  inputFile: "input.txt",
};

export const name = "advent_of_code";
