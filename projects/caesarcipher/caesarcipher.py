{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0e13f072-faa7-4f52-b310-4df9bf6e0d23",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "iuhhFrghFdps\n"
     ]
    }
   ],
   "source": [
    "def caesar(text, shift, encrypt=True):\n",
    "\n",
    "    if not isinstance(shift, int):\n",
    "        return 'Shift must be an integer value.'\n",
    "\n",
    "    if shift < 1 or shift > 25:\n",
    "        return 'Shift must be an integer between 1 and 25.'\n",
    "\n",
    "    alphabet = 'abcdefghijklmnopqrstuvwxyz'\n",
    "\n",
    "    if not encrypt:\n",
    "        shift = - shift\n",
    "    \n",
    "    shifted_alphabet = alphabet[shift:] + alphabet[:shift]\n",
    "    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())\n",
    "    encrypted_text = text.translate(translation_table)\n",
    "    return encrypted_text\n",
    "\n",
    "def encrypt(text, shift):\n",
    "    return caesar(text, shift)\n",
    "    \n",
    "def decrypt(text, shift):\n",
    "    return caesar(text, shift, encrypt=False)\n",
    "encrypted_text = encrypt('freeCodeCamp', 3)\n",
    "print(encrypted_text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5af714f5-6ce3-49b3-b569-d1fb775e5d8b",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
