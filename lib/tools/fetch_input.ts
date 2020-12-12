import { config } from "../../deps.ts";
import { debug } from "../../util.ts";

config({
  export: true,
});

/**
 * Fetches the input from the advent of code website.
 */
const fetchInput = async (
  { year, day, session = Deno.env.get('AOC_SESSION') }: {
    year: number;
    day: number;
    session?: string;
  },
) => {
  debug("Session:", session);
  const inputURL = new URL(`https://adventofcode.com/${year}/day/${day}/input`);
  const headers = new Headers({
    cookie: `session=${session}`,
  });
  const request = new Request(String(inputURL), { headers });
  debug("Fetching input: %O", request);
  const response = await fetch(request);
  debug("Fetching input: %O", response);
  if (!response.ok) {
    throw new Error(
      `Unable to fetch input from ${inputURL}. Was AOC_SESSION set?`,
    );
  }

  const input = await response.text();
  return input;
};

export default fetchInput;
