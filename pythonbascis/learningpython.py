{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ebf5415b-bb1b-430f-8852-ecc8f483b190",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "#Data Types\n",
    "#to check the data type of given variable\n",
    "x=3.14\n",
    "print (type(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "62694bf6-729f-4bae-85b3-9791ae7192c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n",
      "<class 'int'>\n",
      "<class 'float'>\n",
      "<class 'bool'>\n",
      "<class 'NoneType'>\n"
     ]
    }
   ],
   "source": [
    "#list of 5 elements and print the type of each elemet\n",
    "list=[\"hello\",42,3.14,True,None]\n",
    "\n",
    "for item in list:\n",
    "    print(type(item))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9a01dca5-cbdc-4f97-b839-71164a8610fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "133\n"
     ]
    }
   ],
   "source": [
    "#converting string \"123\" into an integer and adding 10 yo it\n",
    "str=\"123\"\n",
    "x=int(str)\n",
    "y=x+10\n",
    "print (y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "614cb572-7c82-4cf7-96e7-776bb8191068",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After swapping:\n",
      "a= 6\n",
      "b= 5\n"
     ]
    }
   ],
   "source": [
    "#swap two variables without using third variable\n",
    "a=5\n",
    "b=6\n",
    "a,b=b,a\n",
    "print(\"After swapping:\")\n",
    "print(\"a=\" ,a)\n",
    "print(\"b=\",b)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58df7bc2-4bed-4952-a706-a0fec9cb907e",
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
