#ifndef MAIN
#define MAIN

#include <iostream>
#include "./main.hh"
#include "spdlog/spdlog.h"

int main(int argc, const char *argv[])
{
#ifdef NDEBUG
  printf("Release configuration!\n");
#else
  printf("Debug configuration!\n");
#endif
  spdlog::warn("hiya5");
  return 0;
}

#endif
