export interface Config {
  year: number;
  day: number;
  session: string;
  dayFilepath: string;
  nameTemplate: string;
  templateFile: string;
  part?: number;
}


export type InitConfig = {
  dayFilePath: string;
  templateFile: string;
  force?: boolean;
};


export enum Month {
  DECEMBER = 11,
}
