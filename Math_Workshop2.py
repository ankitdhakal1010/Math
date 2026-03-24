{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO43OiLGlmWPTPi2mwo8EcQ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ankitdhakal1010/Math/blob/main/Math_Workshop2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*   **Name: Ankit Dhakal**\n",
        "*  **University ID: 2607659**"
      ],
      "metadata": {
        "id": "_dH-3v0_P5nb"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1) Write a Python function that takes a list and return a new list with distinct elements from the first list. Sample List: [1,2,3,3,3,3,4,5] Unique List: [1,2,3,4,5]"
      ],
      "metadata": {
        "id": "dajvN6HZQCH9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def simplifier(n):\n",
        "    temp1= set(n)\n",
        "    temp2= list(temp1)\n",
        "\n",
        "    return temp2\n",
        "\n",
        "print(simplifier([1,1,2,3]))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aKXFTIFOQG-p",
        "outputId": "0d302f63-30db-4e44-b6e6-550f578b2b94"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. Write a Python function that takes a number as a parameter and checks whether the number is prime or not."
      ],
      "metadata": {
        "id": "-EcaNpm4Qcgf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def checkPrime(n):\n",
        "    count = 0\n",
        "    if n == 1 or n == 0:\n",
        "        return False\n",
        "    elif n <0:\n",
        "        return False\n",
        "    for i in range(2,n):\n",
        "        if n % i == 0:\n",
        "            count +=1\n",
        "    if count == 0:\n",
        "        return True\n",
        "    else:\n",
        "        return False\n",
        "checkPrime(2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zcz35CDqQoXG",
        "outputId": "e4db8e31-6643-4120-80cc-bf6bd0bcfd7b"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. Write a program to print twin primes less then 1000. If two consecutive odd numbers are both prime then they are known as twin primes."
      ],
      "metadata": {
        "id": "DHcONjoWSPBY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,1000,2):\n",
        "    if checkPrime(i) and checkPrime(i+2):\n",
        "        print(f\"{i} and {i+2} are twin primes\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yUeCdwnHSTLf",
        "outputId": "eda4194c-3d55-4c9a-f85b-312d613e3a7e"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3 and 5 are twin primes\n",
            "5 and 7 are twin primes\n",
            "11 and 13 are twin primes\n",
            "17 and 19 are twin primes\n",
            "29 and 31 are twin primes\n",
            "41 and 43 are twin primes\n",
            "59 and 61 are twin primes\n",
            "71 and 73 are twin primes\n",
            "101 and 103 are twin primes\n",
            "107 and 109 are twin primes\n",
            "137 and 139 are twin primes\n",
            "149 and 151 are twin primes\n",
            "179 and 181 are twin primes\n",
            "191 and 193 are twin primes\n",
            "197 and 199 are twin primes\n",
            "227 and 229 are twin primes\n",
            "239 and 241 are twin primes\n",
            "269 and 271 are twin primes\n",
            "281 and 283 are twin primes\n",
            "311 and 313 are twin primes\n",
            "347 and 349 are twin primes\n",
            "419 and 421 are twin primes\n",
            "431 and 433 are twin primes\n",
            "461 and 463 are twin primes\n",
            "521 and 523 are twin primes\n",
            "569 and 571 are twin primes\n",
            "599 and 601 are twin primes\n",
            "617 and 619 are twin primes\n",
            "641 and 643 are twin primes\n",
            "659 and 661 are twin primes\n",
            "809 and 811 are twin primes\n",
            "821 and 823 are twin primes\n",
            "827 and 829 are twin primes\n",
            "857 and 859 are twin primes\n",
            "881 and 883 are twin primes\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. A positive integer is called a perfect number if it is equal to the sum of all of its divisors including 1 but excluding the number itself. Write a function sumOfDivisors that takes a positive integer n and returns the sum of all its divisors."
      ],
      "metadata": {
        "id": "QBBUCuZ0ScHI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def sumOfDivisors(n):\n",
        "    sum = 0\n",
        "    for i in range(1,n):\n",
        "        if n % i == 0:\n",
        "            sum += i\n",
        "\n",
        "    return sum\n",
        "\n",
        "sumOfDivisors(6)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LUinCVZCSf7b",
        "outputId": "3a16dc7d-337a-4776-ef19-58028cf8e80e"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "6"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5. The smalles perfect number is 6. Write a program that finds and prints out the next prefect numb"
      ],
      "metadata": {
        "id": "wgxV4MUqUoAP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "i = 6\n",
        "while True:\n",
        "    i += 1\n",
        "    if sumOfDivisors(i) == i:\n",
        "        print(i)\n",
        "        break"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oLTVJBm4Ut0G",
        "outputId": "2173f159-58b5-464c-c4c7-6ca4e4aeffed"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "28\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "6. Write the python program to find the mean median from the following list. Mark[20,30,35,55,70,80,90]"
      ],
      "metadata": {
        "id": "jUsdde0qSmny"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "Mark = [20,30,35,55,70,80,90]\n",
        "\n",
        "Mark = simplifier(Mark)\n",
        "Mark.sort()\n",
        "\n",
        "sum = 0\n",
        "\n",
        "if len(Mark)%2==0:\n",
        "    median = Mark[(len(Mark)+1)//2]\n",
        "else:\n",
        "    median = (Mark[len(Mark)//2] + Mark[(len(Mark)+1)//2])/2\n",
        "\n",
        "print(median)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wF799Uh5So4E",
        "outputId": "c7a31bf2-04b6-4fa7-d255-52a0d82a3dc4"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "62.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "7. Write a function that converts a decimals number to binary number."
      ],
      "metadata": {
        "id": "7A988WFgS302"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def convertDeciToBinary(n):\n",
        "    temp = n\n",
        "    binary = 0\n",
        "    while temp!=0:\n",
        "        a = temp % 2\n",
        "        binary = binary*10 + a\n",
        "        temp = temp // 2\n",
        "    return binary\n",
        "\n",
        "convertDeciToBinary(7)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fb2IWl5_S7XY",
        "outputId": "3450eef5-00d0-40c0-d053-6bd46d680a33"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "111"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "8. Write a function prodDigits() that inputs a number and return the product of digits of that number\n",
        "\n"
      ],
      "metadata": {
        "id": "5d42P4UZS8vJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def prodDigits(n):\n",
        "    pro= 1\n",
        "    temp = n\n",
        "    while temp!=0:\n",
        "        a = temp % 10\n",
        "        pro *= a\n",
        "        temp = temp // 10\n",
        "    return pro\n",
        "\n",
        "prodDigits(123)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-FGpX376TBOY",
        "outputId": "cee02850-9359-4ff3-f4e3-0d35448dc31e"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "6"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "9. Write a function that will take in an unknown number of arguments and multiply all of them together and run the function for these 2 sets of numbers. a.1,2,3,4,5  b.12,13,14"
      ],
      "metadata": {
        "id": "pmp62GMiTEjb"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def product(*numbers):\n",
        "    pro = 1\n",
        "    for i in numbers:\n",
        "        pro *= i\n",
        "    return pro\n",
        "product(1,2,3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CxWpeZBMTIZg",
        "outputId": "e94fd2c6-3953-4b20-9932-0155f07e4e41"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "6"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    }
  ]
}