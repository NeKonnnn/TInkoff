{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b276e1ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import argparse\n",
    "\n",
    "\n",
    "def lev_distance(line1, line2):\n",
    "    n, m = len(line1), len(line2)\n",
    "    if n > m:\n",
    "        line1, line2 = line2, line1\n",
    "        n, m = m, n\n",
    "    current_row = range(n + 1)\n",
    "    for i in range(1, m + 1):\n",
    "        previous_row, current_row = current_row, [i] + [0] * n\n",
    "        for j in range(1, n + 1):\n",
    "            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]\n",
    "            if line1[j - 1] != line2[i - 1]:\n",
    "                change += 1\n",
    "            current_row[j] = min(add, delete, change)\n",
    "    return current_row[n]\n",
    "\n",
    "\n",
    "def compare(line1, line2):\n",
    "    length = max(len(line1), len(line2))\n",
    "    return (1 - lev_distance(line1, line2) / length) * 100\n",
    "\n",
    "\n",
    "parser = argparse.ArgumentParser()\n",
    "parser.add_argument('file1')\n",
    "parser.add_argument('file2')\n",
    "args = parser.parse_args()\n",
    "with open(args.file1, 'r') as f:\n",
    "    lines = f.readlines()\n",
    "documents = []\n",
    "answers = []\n",
    "for line in lines:\n",
    "    line_words = line.split()\n",
    "    documents += line_words\n",
    "for i in range(1, len(documents), 2):\n",
    "    with open(documents[i], 'r', encoding=\"utf-8\") as f:\n",
    "        text1 = f.read()\n",
    "    with open(documents[i - 1], 'r', encoding=\"utf-8\") as f:\n",
    "        text2 = f.read()\n",
    "    with open(args.file2, 'a', encoding=\"utf-8\") as f:\n",
    "        f.write(str(compare(text1, text2)))\n",
    "        f.write('\\n')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
