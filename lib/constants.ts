import { Month } from "../types.ts";

const now = new Date();

export const Defaults = {
  year:
    (now.getMonth() === Month.DECEMBER
      ? now.getFullYear()
      : now.getFullYear() - 1),
  templateFile: "https://raw.githubusercontent.com/bryan-hoang/advent-of-code/main/module/template/day.ts",
  nameTemplate: "day_${num}.ts",
  inputFile: "input.txt",
};

export const name = "advent_of_code";
