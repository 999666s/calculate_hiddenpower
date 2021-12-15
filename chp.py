#!/usr/bin/python3
import asyncio
from re import findall
from sys import argv


types = {
    0: "Bug",
    1: "Dark",
    2: "Dragon",
    3: "Electric",
    4: "Fight",
    5: "Fire",
    6: "Flight",
    7: "Ghost",
    8: "Grass",
    9: "Earth",
    10: "Ice",
    11: "Water",
    12: "Poison",
    13: "Psycho",
    14: "Stone",
    15: "Steel"
}


def hp_from_stats(a, b, c, d, e, f):
    return int(((a + 2*b + 4*c + 8*d + 16*e + 32*f)*15)/63)


def get_stats_from_gen(gen: str) -> list[str]:
    return findall(r'\d+', gen)[0:6]


async def calculate_hiddenpower(gen: str):
    try:
        stats = map(lambda stat: int(stat % 2), map(int, get_stats_from_gen(gen)))
        hp = types[hp_from_stats(*stats)]
    except:
        hp = "Error"
    return hp


async def main():
    gens = argv[1:]
    tasks = [calculate_hiddenpower(gen) for gen in gens]
    results = await asyncio.gather(*tasks)
    for gen, hp in zip(gens, results):
        print(f"{gen}\t{hp}")


if __name__ == "__main__":
    asyncio.run(main())
