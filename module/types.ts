export interface AdventOfCodeConfig {
  year?: number;
  templateFile?: string;
  nameTemplate?: string;
  inputFile?: string;
}

export interface InitOptions extends AdventOfCodeConfig {
  force?: boolean;
}

export type RunOptions = Omit<AdventOfCodeConfig, "templateFile">;

export interface DayModule {
  part1: (input: string) => string;
  part2: (input: string) => string;
}

export type CommandOptionsArgs = [string, string];

export enum Month {
  DECEMBER = 11,
}
