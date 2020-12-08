export interface AdventOfCodeConfig {
  year?: number;
  templateFile?: string;
  nameTemplate?: string;
  inputFile?: string;
}

export interface InitOptions extends AdventOfCodeConfig {
  force?: boolean;
}

export interface RunConfig extends AdventOfCodeConfig {
  part: number;
}

export enum Month {
  DECEMBER = 11,
}
