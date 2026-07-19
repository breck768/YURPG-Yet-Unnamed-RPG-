#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <random>
#include <variant>

using std::string;
using std::vector;
using std::endl;
using std::cout;
using std::cin;
using std::unordered_map;

//Macros used for elemental affinities
#define NONE 0
#define FIRE 1
#define ICE 2
#define THUNDER 3

//Macors used for jobs (calling them jobs instead of classes so it doesnt conflict with c++ classes in some way)
#define WARRIOR 1
#define MAGE 2
#define ROGUE 3

int getRandNum(int min, int max)
{
    std::random_device randy;
    std::mt19937 gen(randy());
    std::uniform_int_distribution<int> distr(min, max);
    int randNum = distr(gen);
    return randNum;
}