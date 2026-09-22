import { test } from "node:test";
import assert from "node:assert/strict";
import { mergeMsdSeries } from "./msdCompare.ts";

test("aligns MSD by actual lag steps without extending short curves", () => {
  const series = [
    { id: "a", status: "done", msd: { points: [
      { step: 100, value: 1 }, { step: 300, value: 3 },
    ] } },
    { id: "b", status: "done", msd: { points: [
      { step: 200, value: 2 }, { step: 300, value: 4 },
    ] } },
    { id: "c", status: "none" },
  ];
  assert.deepEqual(mergeMsdSeries(series), [
    { step: 100, a: 1, b: null },
    { step: 200, b: 2, a: null },
    { step: 300, a: 3, b: 4 },
  ]);
});
