import { debug } from "../util.ts";

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
  { year, day, session }: { year: number; day: number; session: string },
) => {
  if (year < 2015 || year > 2020) {
    throw new Error("Year is not a valid Advent of Code year.");
  }
  if (day < 1 || day > 25) {
    throw new Error("Day is not a valid Advent of Code day.");
  }
  if (!session) {
    throw new Error("Session must be provided.");
  }
  debug("Session:", session);
  const inputURL = new URL(`${ADVENT_HOST}/${year}/day/${day}/input`);
  const headers = new Headers({
    "User-Agent": USER_AGENT,
    Cookie: `session=${session}`,
  });
  const request = new Request(String(inputURL), { headers });
  debug("Request:", request);
  const response = await fetch(request);
  debug("Response:", response);
  const input = await response.text();
  debug("input:", input);
  return input;
};
