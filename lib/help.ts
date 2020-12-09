const help = () => {
  console.log("");
  console.log("Examples:");
  console.log("");
  console.log("    aoc run --day 1 --part 1 'this is my input'");
  console.log("    cat input.txt | aoc run -d 1 -p 1 -");
  console.log("    aoc run -d 1 -p 1 - < input.txt");
  console.log("    aoc run -d 1 -p 1 + --session 'session=asefsafes...'");
  console.log("");
  console.log("Notes:");
  console.log("");
  console.log(
    "    For anything that reaches out to advent-of-code.com, you need to",
  );
  console.log(
    "    provide your session token. You can get this by opening up the",
  );
  console.log(
    "    network tab in the devtools, logging into to adventofcode.com, then",
  );
  console.log("    viewing what gets sent as the `Cookie:` request header on");
  console.log(
    "    subsequent requests. You may pass in the required value using",
  );
  console.log(
    "    `--session [value]` or using the `ADVENT_SESSION` environment",
  );
  console.log("    variable. Note that it likely starts with `session=`");
};

export default help;
