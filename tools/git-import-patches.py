

# Copyright (c) Electron contributors
# Copyright (c) 2013-2020 GitHub Inc.

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import argparse
import sys

from lib import git
from lib.patches import patch_from_dir


def main(argv):
  print("Running git-import-patches")
  parser = argparse.ArgumentParser()
  parser.add_argument("patch_dir",
      help="directory containing patches to apply")
  parser.add_argument("-3", "--3way",
      action="store_true", dest='threeway',
      help="use 3-way merge to resolve conflicts")
  args = parser.parse_args(argv)

  print("Patch directory: " + args.patch_dir)
  print("")
  print("Patch:")
  print(patch_from_dir(args.patch_dir))

  git.import_patches(
      repo='./flock',
      patch_data=patch_from_dir(args.patch_dir),
      threeway=args.threeway
  )


if __name__ == '__main__':
  main(sys.argv[1:])
