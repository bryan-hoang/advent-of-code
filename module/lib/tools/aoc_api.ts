import { config } from "../../deps.ts";
import { debug } from "../../util.ts";

const env = config();

export const ADVENT_HOST = "http://adventofcode.com";
export const USER_AGENT = `deno/${Deno.version.deno} advent_of_code`;

/**
 * @function getInput
 * Gets the input from the advent of code website
 * @param {object} options
 * @param {string | number} options.year - The year to pull input from
 * @param {string | number} options.day - The day to pull input from
 * @param {string} options.session - The advent session cookie to use
 */
export const getInput = async (
  { year, day, session = env.ADVENT_SESSION }: {
    year: number;
    day: number;
    session?: string;
  },
) => {
  debug("Session:", session);
  const inputURL = new URL(`${ADVENT_HOST}/${year}/day/${day}/input`);
  const headers = new Headers({
    "User-Agent": USER_AGENT,
    Cookie: `session=${session}`,
  });
  const request = new Request(String(inputURL), { headers });
  debug("%O", request);
  const response = await fetch(request);
  debug("%O", response);
  const input = await response.text();
  return input;
};
