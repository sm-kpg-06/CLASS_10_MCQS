import json, os

os.makedirs('data', exist_ok=True)

chapters = [
  # -------------------- CHAPTER 1 --------------------
  {
    "chapterNumber": 1,
    "chapterName": "Relations and Functions",
    "icon": "fa-shapes",
    "color": "#4f46e5",
    "description": "Sets, Cartesian products, relations, functions and types of mappings",
    "questions": [
      {
        "id": "m_c1_q1",
        "chapterNumber": 1,
        "chapterName": "Relations and Functions",
        "questionNumber": 1,
        "question": "If n(A × B) = 6 and A = {1, 3}, then n(B) is",
        "options": [
          {"id": "A", "text": "1"},
          {"id": "B", "text": "2"},
          {"id": "C", "text": "3"},
          {"id": "D", "text": "6"}
        ],
        "correctAnswer": "C",
        "explanation": "n(A × B) = n(A) × n(B)\nGiven n(A) = 2 and n(A × B) = 6\n6 = 2 × n(B) ⇒ n(B) = 6 / 2 = 3. [Option (C)]"
      },
      {
        "id": "m_c1_q2",
        "chapterNumber": 1,
        "chapterName": "Relations and Functions",
        "questionNumber": 2,
        "question": "If A = {a, b, p}, B = {2, 3}, C = {p, q, r, s}, then n[(A ∪ C) × B] is",
        "options": [
          {"id": "A", "text": "8"},
          {"id": "B", "text": "20"},
          {"id": "C", "text": "12"},
          {"id": "D", "text": "16"}
        ],
        "correctAnswer": "C",
        "explanation": "A ∪ C = {a, b, p, q, r, s} ⇒ n(A ∪ C) = 6, and n(B) = 2.\nn[(A ∪ C) × B] = n(A ∪ C) × n(B) = 6 × 2 = 12. [Option (C)]"
      },
      {
        "id": "m_c1_q3",
        "chapterNumber": 1,
        "chapterName": "Relations and Functions",
        "questionNumber": 3,
        "question": "If A = {1, 2}, B = {1, 2, 3, 4}, C = {5, 6} and D = {5, 6, 7, 8}, then state which of the following statement is true?",
        "options": [
          {"id": "A", "text": "(A × C) ⊂ (B × D)"},
          {"id": "B", "text": "(B × D) ⊂ (A × C)"},
          {"id": "C", "text": "(A × B) ⊂ (A × D)"},
          {"id": "D", "text": "(D × A) ⊂ (B × A)"}
        ],
        "correctAnswer": "A",
        "explanation": "Since A ⊂ B and C ⊂ D, it follows that (A × C) ⊂ (B × D). [Option (A)]"
      },
      {
        "id": "m_c1_q4",
        "chapterNumber": 1,
        "chapterName": "Relations and Functions",
        "questionNumber": 4,
        "question": "If there are 1024 relations from a set A = {1, 2, 3, 4, 5} to a set B, then the number of elements in B is",
        "options": [
          {"id": "A", "text": "3"},
          {"id": "B", "text": "2"},
          {"id": "C", "text": "4"},
          {"id": "D", "text": "8"}
        ],
        "correctAnswer": "B",
        "explanation": "Total number of relations = 2^(n(A) × n(B)) = 1024 = 2¹⁰.\nSince n(A) = 5, we have 5 × n(B) = 10 ⇒ n(B) = 2. [Option (B)]"
      },
      {
        "id": "m_c1_q5",
        "chapterNumber": 1,
        "chapterName": "Relations and Functions",
        "questionNumber": 5,
        "question": "The range of the relation R = {(x, x²) | x is a prime number less than 13} is",
        "options": [
          {"id": "A", "text": "{2, 3, 5, 7}"},
          {"id": "B", "text": "{2, 3, 5, 7, 11}"},
          {"id": "C", "text": "{4, 9, 25, 49, 121}"},
          {"id": "D", "text": "{1, 4, 9, 25, 49, 121}"}
        ],
        "correctAnswer": "C",
        "explanation": "Prime numbers less than 13 are {2, 3, 5, 7, 11}.\nSquaring each prime: 2² = 4, 3² = 9, 5² = 25, 7² = 49, 11² = 121.\nTherefore, Range of R = {4, 9, 25, 49, 121}. [Option (C)]"
      },
      {
        "id": "m_c1_q6",
        "chapterNumber": 1,
        "chapterName": "Relations and Functions",
        "questionNumber": 6,
        "question": "If the ordered pairs (a + 2, 4) and (5, 2a + b) are equal, then (a, b) is",
        "options": [
          {"id": "A", "text": "(2, -2)"},
          {"id": "B", "text": "(5, 1)"},
          {"id": "C", "text": "(2, 3)"},
          {"id": "D", "text": "(3, -2)"}
        ],
        "correctAnswer": "D",
        "explanation": "Given (a + 2, 4) = (5, 2a + b):\na + 2 = 5 ⇒ a = 3.\n4 = 2a + b ⇒ 4 = 2(3) + b = 6 + b ⇒ b = 4 - 6 = -2.\nThus, (a, b) = (3, -2). [Option (D)]"
      },
      {
        "id": "m_c1_q7",
        "chapterNumber": 1,
        "chapterName": "Relations and Functions",
        "questionNumber": 7,
        "question": "Let n(A) = m and n(B) = n. Then the total number of non-empty relations that can be defined from A to B is",
        "options": [
          {"id": "A", "text": "mⁿ"},
          {"id": "B", "text": "nᵐ"},
          {"id": "C", "text": "2ᵐⁿ - 1"},
          {"id": "D", "text": "2ᵐⁿ"}
        ],
        "correctAnswer": "C",
        "explanation": "Total number of relations from A to B = 2^(mn).\nTotal number of non-empty relations = 2^(mn) - 1. [Option (C)]"
      },
      {
        "id": "m_c1_q8",
        "chapterNumber": 1,
        "chapterName": "Relations and Functions",
        "questionNumber": 8,
        "question": "If {(a, 8), (6, b)} represents an identity function, then the values of a and b are respectively",
        "options": [
          {"id": "A", "text": "(8, 6)"},
          {"id": "B", "text": "(8, 8)"},
          {"id": "C", "text": "(6, 8)"},
          {"id": "D", "text": "(6, 6)"}
        ],
        "correctAnswer": "A",
        "explanation": "An identity function maps every element to itself: f(x) = x.\nSo (a, 8) ⇒ a = 8, and (6, b) ⇒ b = 6.\nThus (a, b) = (8, 6). [Option (A)]"
      },
      {
        "id": "m_c1_q9",
        "chapterNumber": 1,
        "chapterName": "Relations and Functions",
        "questionNumber": 9,
        "question": "Let A = {1, 2, 3, 4} and B = {4, 8, 9, 10}. The function f: A → B given by f = {(1, 4), (2, 8), (3, 9), (4, 10)} is",
        "options": [
          {"id": "A", "text": "a many-one function"},
          {"id": "B", "text": "an identity function"},
          {"id": "C", "text": "an one-to-one function"},
          {"id": "D", "text": "an into function"}
        ],
        "correctAnswer": "C",
        "explanation": "Distinct elements of domain A have distinct images in co-domain B (1→4, 2→8, 3→9, 4→10).\nHence f is a one-to-one (injective) function. [Option (C)]"
      },
      {
        "id": "m_c1_q10",
        "chapterNumber": 1,
        "chapterName": "Relations and Functions",
        "questionNumber": 10,
        "question": "If f(x) = 2x² and g(x) = 1/(3x), then f ∘ g is",
        "options": [
          {"id": "A", "text": "3 / (2x²)"},
          {"id": "B", "text": "2 / (3x²)"},
          {"id": "C", "text": "2 / (9x²)"},
          {"id": "D", "text": "1 / (6x²)"}
        ],
        "correctAnswer": "C",
        "explanation": "(f ∘ g)(x) = f(g(x)) = f(1 / (3x)) = 2 × (1 / (3x))² = 2 × (1 / 9x²) = 2 / (9x²). [Option (C)]"
      },
      {
        "id": "m_c1_q11",
        "chapterNumber": 1,
        "chapterName": "Relations and Functions",
        "questionNumber": 11,
        "question": "If f: A → B is a bijective function and n(B) = 7, then n(A) is",
        "options": [
          {"id": "A", "text": "7"},
          {"id": "B", "text": "49"},
          {"id": "C", "text": "1"},
          {"id": "D", "text": "14"}
        ],
        "correctAnswer": "A",
        "explanation": "A bijection is both one-to-one and onto, meaning every element of A maps to a unique element of B and range = codomain.\nTherefore, n(A) = n(B) = 7. [Option (A)]"
      },
      {
        "id": "m_c1_q12",
        "chapterNumber": 1,
        "chapterName": "Relations and Functions",
        "questionNumber": 12,
        "question": "Let f and g be two functions defined by f = {(0, 1), (2, 0), (3, -4), (4, 2), (5, 7)} and g = {(0, 2), (1, 0), (2, 4), (-4, 2), (7, 0)}. Then the range of f ∘ g is",
        "options": [
          {"id": "A", "text": "{0, 2, 3, 4, 5}"},
          {"id": "B", "text": "{-4, 1, 0, 2, 7}"},
          {"id": "C", "text": "{1, 2, 3, 4, 5}"},
          {"id": "D", "text": "{0, 1, 2}"}
        ],
        "correctAnswer": "D",
        "explanation": "(f ∘ g)(0) = f(g(0)) = f(2) = 0\n(f ∘ g)(1) = f(g(1)) = f(0) = 1\n(f ∘ g)(2) = f(g(2)) = f(4) = 2\n(f ∘ g)(-4) = f(g(-4)) = f(2) = 0\n(f ∘ g)(7) = f(g(7)) = f(0) = 1\nThus, Range of f ∘ g = {0, 1, 2}. [Option (D)]"
      },
      {
        "id": "m_c1_q13",
        "chapterNumber": 1,
        "chapterName": "Relations and Functions",
        "questionNumber": 13,
        "question": "If f(x) = √(1 + x²), then",
        "options": [
          {"id": "A", "text": "f(xy) = f(x) · f(y)"},
          {"id": "B", "text": "f(xy) ≥ f(x) · f(y)"},
          {"id": "C", "text": "f(xy) ≤ f(x) · f(y)"},
          {"id": "D", "text": "None of these"}
        ],
        "correctAnswer": "C",
        "explanation": "f(xy) = √(1 + x²y²)\nf(x) · f(y) = √(1 + x²) · √(1 + y²) = √(1 + x² + y² + x²y²)\nSince 1 + x²y² ≤ 1 + x² + y² + x²y², taking square roots gives f(xy) ≤ f(x) · f(y). [Option (C)]"
      },
      {
        "id": "m_c1_q14",
        "chapterNumber": 1,
        "chapterName": "Relations and Functions",
        "questionNumber": 14,
        "question": "If g = {(1, 1), (2, 3), (3, 5), (4, 7)} is a function given by g(x) = αx + β, then the values of α and β are",
        "options": [
          {"id": "A", "text": "(-1, 2)"},
          {"id": "B", "text": "(2, -1)"},
          {"id": "C", "text": "(-1, -2)"},
          {"id": "D", "text": "(1, 2)"}
        ],
        "correctAnswer": "B",
        "explanation": "For x = 1: g(1) = α(1) + β = 1 ⇒ α + β = 1  --- (1)\nFor x = 2: g(2) = α(2) + β = 3 ⇒ 2α + β = 3  --- (2)\nSubtracting (1) from (2): α = 2.\nFrom (1): 2 + β = 1 ⇒ β = -1.\nThus (α, β) = (2, -1). [Option (B)]"
      },
      {
        "id": "m_c1_q15",
        "chapterNumber": 1,
        "chapterName": "Relations and Functions",
        "questionNumber": 15,
        "question": "The function f(x) = (x + 1)³ - (x - 1)³ is",
        "options": [
          {"id": "A", "text": "linear"},
          {"id": "B", "text": "cubic"},
          {"id": "C", "text": "reciprocal"},
          {"id": "D", "text": "quadratic"}
        ],
        "correctAnswer": "D",
        "explanation": "Expanding using algebraic identities:\nf(x) = (x³ + 3x² + 3x + 1) - (x³ - 3x² + 3x - 1)\n     = 6x² + 2\nThe highest power of x is 2, hence f(x) is a quadratic function. [Option (D)]"
      }
    ]
  },

  # -------------------- CHAPTER 2 --------------------
  {
    "chapterNumber": 2,
    "chapterName": "Numbers and Sequences",
    "icon": "fa-list-ol",
    "color": "#0284c7",
    "description": "Euclid's division lemma, Fundamental theorem of arithmetic, Modular arithmetic, AP, GP and Special Series",
    "questions": [
      {
        "id": "m_c2_q1",
        "chapterNumber": 2,
        "chapterName": "Numbers and Sequences",
        "questionNumber": 1,
        "question": "Euclid’s division lemma states that for positive integers a and b, there exist unique integers q and r such that a = bq + r, where r must satisfy",
        "options": [
          {"id": "A", "text": "1 < r < b"},
          {"id": "B", "text": "0 < r < b"},
          {"id": "C", "text": "0 ≤ r < b"},
          {"id": "D", "text": "0 < r ≤ b"}
        ],
        "correctAnswer": "C",
        "explanation": "By Euclid's division lemma, the remainder r is a non-negative integer strictly less than the divisor b, so 0 ≤ r < b. [Option (C)]"
      },
      {
        "id": "m_c2_q2",
        "chapterNumber": 2,
        "chapterName": "Numbers and Sequences",
        "questionNumber": 2,
        "question": "If the cube of any positive integer is divided by 9, then the possible remainders are",
        "options": [
          {"id": "A", "text": "0, 1, 8"},
          {"id": "B", "text": "1, 4, 8"},
          {"id": "C", "text": "0, 1, 3"},
          {"id": "D", "text": "1, 3, 5"}
        ],
        "correctAnswer": "A",
        "explanation": "Let x be any positive integer.\nWhen x = 1, 1³ = 1 ≡ 1 (mod 9);\nWhen x = 2, 2³ = 8 ≡ 8 (mod 9);\nWhen x = 3, 3³ = 27 ≡ 0 (mod 9);\nWhen x = 4, 4³ = 64 = 7 × 9 + 1 ≡ 1 (mod 9);\nWhen x = 5, 5³ = 125 = 13 × 9 + 8 ≡ 8 (mod 9);\nWhen x = 6, 6³ = 216 ≡ 0 (mod 9).\nThus the possible remainders are 0, 1, 8. [Option (A)]"
      },
      {
        "id": "m_c2_q3",
        "chapterNumber": 2,
        "chapterName": "Numbers and Sequences",
        "questionNumber": 3,
        "question": "If the H.C.F. of 65 and 117 is expressible in the form 65m - 117, then the value of m is",
        "options": [
          {"id": "A", "text": "4"},
          {"id": "B", "text": "2"},
          {"id": "C", "text": "1"},
          {"id": "D", "text": "3"}
        ],
        "correctAnswer": "B",
        "explanation": "65 = 13 × 5 and 117 = 13 × 9, so HCF(65, 117) = 13.\nGiven: 65m - 117 = 13 ⇒ 65m = 130 ⇒ m = 130 / 65 = 2. [Option (B)]"
      },
      {
        "id": "m_c2_q4",
        "chapterNumber": 2,
        "chapterName": "Numbers and Sequences",
        "questionNumber": 4,
        "question": "The sum of the exponents of the prime factors in the prime factorization of 1729 is",
        "options": [
          {"id": "A", "text": "1"},
          {"id": "B", "text": "2"},
          {"id": "C", "text": "3"},
          {"id": "D", "text": "4"}
        ],
        "correctAnswer": "C",
        "explanation": "1729 (the Hardy-Ramanujan number) = 7 × 13 × 19 = 7¹ × 13¹ × 19¹.\nSum of exponents = 1 + 1 + 1 = 3. [Option (C)]"
      },
      {
        "id": "m_c2_q5",
        "chapterNumber": 2,
        "chapterName": "Numbers and Sequences",
        "questionNumber": 5,
        "question": "The least number that is divisible by all the numbers from 1 to 10 (both inclusive) is",
        "options": [
          {"id": "A", "text": "2025"},
          {"id": "B", "text": "5220"},
          {"id": "C", "text": "5025"},
          {"id": "D", "text": "2520"}
        ],
        "correctAnswer": "D",
        "explanation": "Required number = LCM(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)\n= 2³ × 3² × 5 × 7 = 8 × 9 × 5 × 7 = 2520. [Option (D)]"
      },
      {
        "id": "m_c2_q6",
        "chapterNumber": 2,
        "chapterName": "Numbers and Sequences",
        "questionNumber": 6,
        "question": "If k is a positive integer and 7^(4k) ≡ x (mod 100), then x is",
        "options": [
          {"id": "A", "text": "1"},
          {"id": "B", "text": "2"},
          {"id": "C", "text": "3"},
          {"id": "D", "text": "4"}
        ],
        "correctAnswer": "A",
        "explanation": "7⁴ = 2401 ≡ 1 (mod 100).\n7^(4k) = (7⁴)^k ≡ 1^k ≡ 1 (mod 100). So x = 1. [Option (A)]"
      },
      {
        "id": "m_c2_q7",
        "chapterNumber": 2,
        "chapterName": "Numbers and Sequences",
        "questionNumber": 7,
        "question": "Given F₁ = 1, F₂ = 3 and Fₙ = Fₙ₋₁ + Fₙ₋₂, then F₅ is",
        "options": [
          {"id": "A", "text": "3"},
          {"id": "B", "text": "5"},
          {"id": "C", "text": "8"},
          {"id": "D", "text": "11"}
        ],
        "correctAnswer": "D",
        "explanation": "F₁ = 1, F₂ = 3\nF₃ = F₂ + F₁ = 3 + 1 = 4\nF₄ = F₃ + F₂ = 4 + 3 = 7\nF₅ = F₄ + F₃ = 7 + 4 = 11. [Option (D)]"
      },
      {
        "id": "m_c2_q8",
        "chapterNumber": 2,
        "chapterName": "Numbers and Sequences",
        "questionNumber": 8,
        "question": "The first term of an arithmetic progression is unity and the common difference is 4. Which of the following will be a term of this A.P.?",
        "options": [
          {"id": "A", "text": "4551"},
          {"id": "B", "text": "10091"},
          {"id": "C", "text": "7881"},
          {"id": "D", "text": "13531"}
        ],
        "correctAnswer": "C",
        "explanation": "tₙ = a + (n - 1)d = 1 + (n - 1)4 = 4n - 3.\nThus, tₙ ≡ 1 (mod 4), meaning (tₙ - 1) must be divisible by 4.\nChecking 7881: 7881 - 1 = 7880, which is divisible by 4 (7880 / 4 = 1970 ⇒ n = 1971 is an integer). [Option (C)]"
      },
      {
        "id": "m_c2_q9",
        "chapterNumber": 2,
        "chapterName": "Numbers and Sequences",
        "questionNumber": 9,
        "question": "If 6 times of 6th term of an A.P. is equal to 7 times the 7th term, then the 13th term of the A.P. is",
        "options": [
          {"id": "A", "text": "0"},
          {"id": "B", "text": "6"},
          {"id": "C", "text": "7"},
          {"id": "D", "text": "13"}
        ],
        "correctAnswer": "A",
        "explanation": "6 × t₆ = 7 × t₇ ⇒ 6(a + 5d) = 7(a + 6d)\n⇒ 6a + 30d = 7a + 42d ⇒ a + 12d = 0.\nSince t₁₃ = a + 12d, we have t₁₃ = 0. [Option (A)]"
      },
      {
        "id": "m_c2_q10",
        "chapterNumber": 2,
        "chapterName": "Numbers and Sequences",
        "questionNumber": 10,
        "question": "An A.P. consists of 31 terms. If its 16th term is m, then the sum of all the terms of this A.P. is",
        "options": [
          {"id": "A", "text": "16m"},
          {"id": "B", "text": "62m"},
          {"id": "C", "text": "31m"},
          {"id": "D", "text": "31/2 m"}
        ],
        "correctAnswer": "C",
        "explanation": "t₁₆ = a + 15d = m.\nS₃₁ = (31 / 2)[2a + (31 - 1)d] = (31 / 2)[2a + 30d] = 31(a + 15d) = 31m. [Option (C)]"
      },
      {
        "id": "m_c2_q11",
        "chapterNumber": 2,
        "chapterName": "Numbers and Sequences",
        "questionNumber": 11,
        "question": "In an A.P., the first term is 1, the common difference is 4 and Sₙ = 120, then n is",
        "options": [
          {"id": "A", "text": "6"},
          {"id": "B", "text": "7"},
          {"id": "C", "text": "8"},
          {"id": "D", "text": "9"}
        ],
        "correctAnswer": "C",
        "explanation": "Sₙ = (n / 2)[2(1) + (n - 1)4] = 120\n⇒ (n / 2)[4n - 2] = 120 ⇒ n(2n - 1) = 120\n⇒ 2n² - n - 120 = 0 ⇒ (n - 8)(2n + 15) = 0 ⇒ n = 8. [Option (C)]"
      },
      {
        "id": "m_c2_q12",
        "chapterNumber": 2,
        "chapterName": "Numbers and Sequences",
        "questionNumber": 12,
        "question": "If A = 2⁶⁵ and B = 2⁶⁴ + 2⁶³ + 2⁶² + ... + 2⁰, which of the following is true?",
        "options": [
          {"id": "A", "text": "B is 2⁶⁴ more than A"},
          {"id": "B", "text": "A and B are equal"},
          {"id": "C", "text": "B is larger than A by 1"},
          {"id": "D", "text": "A is larger than B by 1"}
        ],
        "correctAnswer": "D",
        "explanation": "B is a G.P. with a = 1, r = 2, and 65 terms.\nB = 1(2⁶⁵ - 1) / (2 - 1) = 2⁶⁵ - 1 = A - 1.\nTherefore, A = B + 1, so A is larger than B by 1. [Option (D)]"
      },
      {
        "id": "m_c2_q13",
        "chapterNumber": 2,
        "chapterName": "Numbers and Sequences",
        "questionNumber": 13,
        "question": "The next term of the sequence 3/16, 1/8, 1/12, 1/18, ... is",
        "options": [
          {"id": "A", "text": "1/24"},
          {"id": "B", "text": "1/27"},
          {"id": "C", "text": "2/3"},
          {"id": "D", "text": "1/81"}
        ],
        "correctAnswer": "B",
        "explanation": "Common ratio r = (1/8) / (3/16) = (1/8) × (16/3) = 2/3.\nNext term = (1/18) × (2/3) = 2 / 54 = 1/27. [Option (B)]"
      },
      {
        "id": "m_c2_q14",
        "chapterNumber": 2,
        "chapterName": "Numbers and Sequences",
        "questionNumber": 14,
        "question": "If the sequence t₁, t₂, t₃, ... is an A.P., then the sequence t₆, t₁₂, t₁₈, ... is",
        "options": [
          {"id": "A", "text": "a G.P."},
          {"id": "B", "text": "an A.P."},
          {"id": "C", "text": "neither A.P. nor G.P."},
          {"id": "D", "text": "a constant sequence"}
        ],
        "correctAnswer": "B",
        "explanation": "Since the indices 6, 12, 18, ... form an A.P. with common difference 6, the corresponding terms have common difference 6d, which forms an A.P. [Option (B)]"
      },
      {
        "id": "m_c2_q15",
        "chapterNumber": 2,
        "chapterName": "Numbers and Sequences",
        "questionNumber": 15,
        "question": "The value of (1³ + 2³ + 3³ + ... + 15³) - (1 + 2 + 3 + ... + 15) is",
        "options": [
          {"id": "A", "text": "14400"},
          {"id": "B", "text": "14200"},
          {"id": "C", "text": "14280"},
          {"id": "D", "text": "14520"}
        ],
        "correctAnswer": "C",
        "explanation": "Sum of first 15 cubes = [15 × 16 / 2]² = 120² = 14400.\nSum of first 15 natural numbers = 15 × 16 / 2 = 120.\nDifference = 14400 - 120 = 14280. [Option (C)]"
      }
    ]
  },

  # -------------------- CHAPTER 3 --------------------
  {
    "chapterNumber": 3,
    "chapterName": "Algebra",
    "icon": "fa-square-root-variable",
    "color": "#059669",
    "description": "Linear equations, polynomials, rational expressions, quadratic equations, matrices",
    "questions": [
      {
        "id": "m_c3_q1",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 1,
        "question": "A system of three linear equations in three variables is inconsistent if the corresponding planes",
        "options": [
          {"id": "A", "text": "intersect only at a point"},
          {"id": "B", "text": "intersect in a line"},
          {"id": "C", "text": "coincide with each other"},
          {"id": "D", "text": "neither intersect in a line nor coincide"}
        ],
        "correctAnswer": "D",
        "explanation": "Inconsistency implies there is no common solution, meaning the three planes have no point or line in common. [Option (D)]"
      },
      {
        "id": "m_c3_q2",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 2,
        "question": "The solution of the system x + y - 3z = -6, -7y + 7z = 7, 3z = 9 is",
        "options": [
          {"id": "A", "text": "x = 1, y = 2, z = 3"},
          {"id": "B", "text": "x = -1, y = 2, z = 3"},
          {"id": "C", "text": "x = -1, y = -2, z = 3"},
          {"id": "D", "text": "x = 1, y = -2, z = 3"}
        ],
        "correctAnswer": "A",
        "explanation": "From 3z = 9 ⇒ z = 3.\nFrom -7y + 7(3) = 7 ⇒ -7y + 21 = 7 ⇒ -7y = -14 ⇒ y = 2.\nFrom x + 2 - 3(3) = -6 ⇒ x + 2 - 9 = -6 ⇒ x - 7 = -6 ⇒ x = 1.\nThus x = 1, y = 2, z = 3. [Option (A)]"
      },
      {
        "id": "m_c3_q3",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 3,
        "question": "If (x - 6) is a factor of x² - kx - 6, then the value of k is",
        "options": [
          {"id": "A", "text": "3"},
          {"id": "B", "text": "5"},
          {"id": "C", "text": "6"},
          {"id": "D", "text": "8"}
        ],
        "correctAnswer": "B",
        "explanation": "By factor theorem, P(6) = 0 ⇒ 6² - 6k - 6 = 0 ⇒ 36 - 6 - 6k = 0 ⇒ 30 = 6k ⇒ k = 5. [Option (B)]"
      },
      {
        "id": "m_c3_q4",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 4,
        "question": "The quotient of (3y - 3)/y divided by (7y - 7)/(3y²) is",
        "options": [
          {"id": "A", "text": "9y / 7"},
          {"id": "B", "text": "9y³ / (21y - 21)"},
          {"id": "C", "text": "21(y² - 2y + 1) / (3y³)"},
          {"id": "D", "text": "7 / (9y)"}
        ],
        "correctAnswer": "A",
        "explanation": "[(3y - 3)/y] ÷ [(7y - 7)/(3y²)] = [3(y - 1)/y] × [3y² / 7(y - 1)] = (3 × 3y) / 7 = 9y / 7. [Option (A)]"
      },
      {
        "id": "m_c3_q5",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 5,
        "question": "y² + 1/y² is not equal to",
        "options": [
          {"id": "A", "text": "(y⁴ + 1) / y²"},
          {"id": "B", "text": "[ (y + 1)/y ]²"},
          {"id": "C", "text": "[ y - (1/y) ]² + 2"},
          {"id": "D", "text": "[ y + (1/y) ]² - 2"}
        ],
        "correctAnswer": "B",
        "explanation": "[ (y + 1)/y ]² = [(y² + 2y + 1)/y²] = y² + 2/y + 1/y², which is not equal to y² + 1/y².\nNotice [y + 1/y]² - 2 = y² + 1/y², so Option B is the incorrect expression. [Option (B)]"
      },
      {
        "id": "m_c3_q6",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 6,
        "question": "x/(x² - 25) - 8/(x² + 6x + 5) is equal to",
        "options": [
          {"id": "A", "text": "(x² - 7x + 40) / (x - 5)"},
          {"id": "B", "text": "(x² + 7x + 40) / [(x - 5)(x + 5)]"},
          {"id": "C", "text": "(x² - 7x + 40) / [(x² - 25)(x + 1)]"},
          {"id": "D", "text": "(x² + 10) / [(x² - 25)(x + 1)]"}
        ],
        "correctAnswer": "C",
        "explanation": "x / [(x - 5)(x + 5)] - 8 / [(x + 5)(x + 1)]\n= [x(x + 1) - 8(x - 5)] / [(x - 5)(x + 5)(x + 1)]\n= (x² + x - 8x + 40) / [(x² - 25)(x + 1)]\n= (x² - 7x + 40) / [(x² - 25)(x + 1)]. [Option (C)]"
      },
      {
        "id": "m_c3_q7",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 7,
        "question": "The square root of (256 x⁸ y⁴ z¹⁰) / (25 x⁶ y⁶ z⁶) is equal to",
        "options": [
          {"id": "A", "text": "(16/5) |(x² z⁴) / y²|"},
          {"id": "B", "text": "(16/5) |(y²) / (x² z⁴)|"},
          {"id": "C", "text": "(16/5) |(y) / (x z²)|"},
          {"id": "D", "text": "(16/5) |(x z²) / y|"}
        ],
        "correctAnswer": "D",
        "explanation": "Simplifying the fraction inside:\n(256/25) × x^(8-6) × y^(4-6) × z^(10-6) = (256/25) × (x² z⁴ / y²)\nTaking square root gives (16/5) |(x z²) / y|. [Option (D)]"
      },
      {
        "id": "m_c3_q8",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 8,
        "question": "Which of the following should be added to make x⁴ + 64 a perfect square?",
        "options": [
          {"id": "A", "text": "4x²"},
          {"id": "B", "text": "16x²"},
          {"id": "C", "text": "8x²"},
          {"id": "D", "text": "-8x²"}
        ],
        "correctAnswer": "B",
        "explanation": "x⁴ + 64 = (x²)² + 8².\nTo make it a perfect square (x² + 8)², we need 2(x²)(8) = 16x².\nTherefore, 16x² must be added. [Option (B)]"
      },
      {
        "id": "m_c3_q9",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 9,
        "question": "The solution of (2x - 1)² = 9 is equal to",
        "options": [
          {"id": "A", "text": "-1 only"},
          {"id": "B", "text": "2 only"},
          {"id": "C", "text": "-1, 2"},
          {"id": "D", "text": "None of these"}
        ],
        "correctAnswer": "C",
        "explanation": "(2x - 1)² = 9 ⇒ 2x - 1 = ±3\nIf 2x - 1 = 3 ⇒ 2x = 4 ⇒ x = 2.\nIf 2x - 1 = -3 ⇒ 2x = -2 ⇒ x = -1.\nThus x = -1, 2. [Option (C)]"
      },
      {
        "id": "m_c3_q10",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 10,
        "question": "If 4x⁴ - 24x³ + 76x² + ax + b is a perfect square, the values of a and b are",
        "options": [
          {"id": "A", "text": "100, 120"},
          {"id": "B", "text": "10, 12"},
          {"id": "C", "text": "-120, 100"},
          {"id": "D", "text": "12, 10"}
        ],
        "correctAnswer": "C",
        "explanation": "By square root long division method for polynomials:\n(2x² - 6x + 10)² = 4x⁴ - 24x³ + 76x² - 120x + 100.\nComparing coefficients with ax + b: a = -120, b = 100. [Option (C)]"
      },
      {
        "id": "m_c3_q11",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 11,
        "question": "If the roots of the equation q²x² + p²x + r² = 0 are the squares of the roots of the equation qx² + px + r = 0, then q, p, r are in",
        "options": [
          {"id": "A", "text": "A.P."},
          {"id": "B", "text": "G.P."},
          {"id": "C", "text": "Both A.P. and G.P."},
          {"id": "D", "text": "None of these"}
        ],
        "correctAnswer": "B",
        "explanation": "If α and β are roots of qx² + px + r = 0, then α + β = -p/q and αβ = r/q.\nFor roots α², β²: sum = α² + β² = (α+β)² - 2αβ = p²/q² - 2r/q.\nIn q²x² + p²x + r² = 0, sum = -p²/q².\nEquating gives p²/q² = r/q ⇒ p² = qr, which proves q, p, r are in G.P. [Option (B)]"
      },
      {
        "id": "m_c3_q12",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 12,
        "question": "Graph of a linear equation in two variables is a",
        "options": [
          {"id": "A", "text": "straight line"},
          {"id": "B", "text": "circle"},
          {"id": "C", "text": "parabola"},
          {"id": "D", "text": "hyperbola"}
        ],
        "correctAnswer": "A",
        "explanation": "A first-degree polynomial in two variables (ax + by + c = 0) represents a straight line. [Option (A)]"
      },
      {
        "id": "m_c3_q13",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 13,
        "question": "The graph y = x² + 4x + 4 cuts the X-axis at",
        "options": [
          {"id": "A", "text": "no point"},
          {"id": "B", "text": "1 point"},
          {"id": "C", "text": "3 points"},
          {"id": "D", "text": "2 points"}
        ],
        "correctAnswer": "B",
        "explanation": "Setting y = 0 gives x² + 4x + 4 = 0 ⇒ (x + 2)² = 0 ⇒ x = -2 (repeated root).\nSince there is only one real root, the parabola touches the X-axis at exactly 1 point (-2, 0). [Option (B)]"
      },
      {
        "id": "m_c3_q14",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 14,
        "question": "For a given matrix A of order 3 × 4, the order of the transpose matrix Aᵀ is",
        "options": [
          {"id": "A", "text": "2 × 3"},
          {"id": "B", "text": "3 × 2"},
          {"id": "C", "text": "3 × 4"},
          {"id": "D", "text": "4 × 3"}
        ],
        "correctAnswer": "D",
        "explanation": "If matrix A has order m × n, then its transpose Aᵀ has order n × m.\nHere, m = 3 and n = 4, so order of Aᵀ is 4 × 3. [Option (D)]"
      },
      {
        "id": "m_c3_q15",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 15,
        "question": "If A is a 2 × 3 matrix and B is a 3 × 4 matrix, how many columns does the matrix AB have?",
        "options": [
          {"id": "A", "text": "3"},
          {"id": "B", "text": "4"},
          {"id": "C", "text": "2"},
          {"id": "D", "text": "5"}
        ],
        "correctAnswer": "B",
        "explanation": "The product of an m × k matrix and a k × n matrix has order m × n.\nHere (2 × 3) × (3 × 4) produces a matrix of order 2 × 4, which has 4 columns. [Option (B)]"
      },
      {
        "id": "m_c3_q16",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 16,
        "question": "A matrix whose number of columns and rows are not equal is called",
        "options": [
          {"id": "A", "text": "a diagonal matrix"},
          {"id": "B", "text": "a rectangular matrix"},
          {"id": "C", "text": "a square matrix"},
          {"id": "D", "text": "an identity matrix"}
        ],
        "correctAnswer": "B",
        "explanation": "A matrix in which the number of rows is not equal to the number of columns (m ≠ n) is called a rectangular matrix. [Option (B)]"
      },
      {
        "id": "m_c3_q17",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 17,
        "question": "Transpose of a column matrix of order n × 1 is a",
        "options": [
          {"id": "A", "text": "unit matrix"},
          {"id": "B", "text": "diagonal matrix"},
          {"id": "C", "text": "column matrix"},
          {"id": "D", "text": "row matrix"}
        ],
        "correctAnswer": "D",
        "explanation": "A column matrix of order n × 1 when transposed becomes a 1 × n matrix, which is a row matrix. [Option (D)]"
      },
      {
        "id": "m_c3_q18",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 18,
        "question": "Find the matrix X if 2X + [[1, 3], [5, 7]] = [[5, 7], [9, 5]]",
        "options": [
          {"id": "A", "text": "[[1, 2], [2, 1]]"},
          {"id": "B", "text": "[[2, 2], [2, -1]]"},
          {"id": "C", "text": "[[2, 1], [2, 2]]"},
          {"id": "D", "text": "[[2, -1], [2, 2]]"}
        ],
        "correctAnswer": "B",
        "explanation": "2X = [[5, 7], [9, 5]] - [[1, 3], [5, 7]] = [[4, 4], [4, -2]].\nX = (1/2) [[4, 4], [4, -2]] = [[2, 2], [2, -1]]. [Option (B)]"
      },
      {
        "id": "m_c3_q19",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 19,
        "question": "If matrix A has order 3 × 2 and B has order 3 × 3, which of the following products are defined? (i) A²  (ii) B²  (iii) AB  (iv) BA",
        "options": [
          {"id": "A", "text": "(i) and (ii) only"},
          {"id": "B", "text": "(ii) and (iii) only"},
          {"id": "C", "text": "(ii) and (iv) only"},
          {"id": "D", "text": "All of these"}
        ],
        "correctAnswer": "C",
        "explanation": "For matrix multiplication, the number of columns in the 1st matrix must equal the number of rows in the 2nd.\n- A²: (3×2) × (3×2) - Not possible\n- B²: (3×3) × (3×3) - Possible\n- AB: (3×2) × (3×3) - Not possible (2 ≠ 3)\n- BA: (3×3) × (3×2) - Possible (3 = 3)\nThus only (ii) and (iv) are defined. [Option (C)]"
      },
      {
        "id": "m_c3_q20",
        "chapterNumber": 3,
        "chapterName": "Algebra",
        "questionNumber": 20,
        "question": "If A = [[1, 2, 3], [3, 2, 1]], B = [[1, 0], [2, -1], [0, 2]] and C = [[0, 1], [-2, 5]], which of the statements are correct? (i) AB + C = [[5, 5], [5, 5]]  (ii) BC is order 3 × 2",
        "options": [
          {"id": "A", "text": "(i) and (ii) only"},
          {"id": "B", "text": "(ii) only"},
          {"id": "C", "text": "(i) only"},
          {"id": "D", "text": "None of these"}
        ],
        "correctAnswer": "A",
        "explanation": "AB = [[1(1)+2(2)+3(0), 1(0)+2(-1)+3(2)], [3(1)+2(2)+1(0), 3(0)+2(-1)+1(2)]] = [[5, 4], [7, 0]].\nAB + C = [[5+0, 4+1], [7+(-2), 0+5]] = [[5, 5], [5, 5]]. (Statement i is correct).\nB has order 3 × 2 and C has order 2 × 2, so BC has order 3 × 2 (Statement ii is correct).\nThus (i) and (ii) are both correct. [Option (A)]"
      }
    ]
  },

  # -------------------- CHAPTER 4 --------------------
  {
    "chapterNumber": 4,
    "chapterName": "Geometry",
    "icon": "fa-draw-polygon",
    "color": "#d97706",
    "description": "Similar triangles, Thales theorem, Angle bisector theorem, Pythagoras theorem, Tangents to circle",
    "questions": [
      {
        "id": "m_c4_q1",
        "chapterNumber": 4,
        "chapterName": "Geometry",
        "questionNumber": 1,
        "question": "If triangles ABC and EDF are similar such that AB/ED = BC/DF, then",
        "options": [
          {"id": "A", "text": "∠B = ∠E"},
          {"id": "B", "text": "∠A = ∠D"},
          {"id": "C", "text": "∠B = ∠D"},
          {"id": "D", "text": "∠A = ∠F"}
        ],
        "correctAnswer": "C",
        "explanation": "The included angle between sides AB and BC in ΔABC is ∠B. The included angle between sides ED and DF in ΔEDF is ∠D.\nBy SAS similarity criterion, ΔABC ~ ΔEDF if ∠B = ∠D. [Option (C)]"
      },
      {
        "id": "m_c4_q2",
        "chapterNumber": 4,
        "chapterName": "Geometry",
        "questionNumber": 2,
        "question": "In ΔLMN, ∠L = 60°, ∠M = 50°. If ΔLMN ~ ΔPQR, then the value of ∠R is",
        "options": [
          {"id": "A", "text": "40°"},
          {"id": "B", "text": "70°"},
          {"id": "C", "text": "30°"},
          {"id": "D", "text": "110°"}
        ],
        "correctAnswer": "B",
        "explanation": "In ΔLMN, sum of angles = 180° ⇒ ∠N = 180° - (60° + 50°) = 70°.\nSince ΔLMN ~ ΔPQR, corresponding angles are equal, so ∠R = ∠N = 70°. [Option (B)]"
      },
      {
        "id": "m_c4_q3",
        "chapterNumber": 4,
        "chapterName": "Geometry",
        "questionNumber": 3,
        "question": "If ΔABC is an isosceles triangle with ∠C = 90° and AC = 5 cm, then AB is",
        "options": [
          {"id": "A", "text": "2.5 cm"},
          {"id": "B", "text": "5 cm"},
          {"id": "C", "text": "10 cm"},
          {"id": "D", "text": "5√2 cm"}
        ],
        "correctAnswer": "D",
        "explanation": "Since ΔABC is isosceles with right angle at C, BC = AC = 5 cm.\nBy Pythagoras theorem: AB² = AC² + BC² = 5² + 5² = 25 + 25 = 50.\nAB = √50 = 5√2 cm. [Option (D)]"
      },
      {
        "id": "m_c4_q4",
        "chapterNumber": 4,
        "chapterName": "Geometry",
        "questionNumber": 4,
        "question": "In ΔPQR, ST || QR, PS = 2 cm and SQ = 3 cm. Then the ratio of the area of ΔPQR to the area of ΔPST is",
        "options": [
          {"id": "A", "text": "25 : 4"},
          {"id": "B", "text": "25 : 7"},
          {"id": "C", "text": "25 : 11"},
          {"id": "D", "text": "25 : 13"}
        ],
        "correctAnswer": "A",
        "explanation": "PQ = PS + SQ = 2 + 3 = 5 cm.\nSince ST || QR, ΔPQR ~ ΔPST.\nRatio of areas = (PQ / PS)² = (5 / 2)² = 25 / 4 = 25 : 4. [Option (A)]"
      },
      {
        "id": "m_c4_q5",
        "chapterNumber": 4,
        "chapterName": "Geometry",
        "questionNumber": 5,
        "question": "The perimeters of two similar triangles ΔABC and ΔPQR are 36 cm and 24 cm respectively. If PQ = 10 cm, then the length of AB is",
        "options": [
          {"id": "A", "text": "6.6 cm"},
          {"id": "B", "text": "10/3 cm"},
          {"id": "C", "text": "60 cm"},
          {"id": "D", "text": "15 cm"}
        ],
        "correctAnswer": "D",
        "explanation": "The ratio of perimeters of similar triangles equals the ratio of their corresponding sides:\nAB / PQ = Perimeter(ΔABC) / Perimeter(ΔPQR) ⇒ AB / 10 = 36 / 24 = 3 / 2\nAB = 10 × (3 / 2) = 15 cm. [Option (D)]"
      },
      {
        "id": "m_c4_q6",
        "chapterNumber": 4,
        "chapterName": "Geometry",
        "questionNumber": 6,
        "question": "In ΔABC, DE || BC, AB = 3.6 cm, AC = 2.4 cm and AD = 2.1 cm. The length of AE is",
        "options": [
          {"id": "A", "text": "1.4 cm"},
          {"id": "B", "text": "1.8 cm"},
          {"id": "C", "text": "1.2 cm"},
          {"id": "D", "text": "1.05 cm"}
        ],
        "correctAnswer": "A",
        "explanation": "By Basic Proportionality Theorem (Thales Theorem):\nAD / AB = AE / AC ⇒ 2.1 / 3.6 = AE / 2.4\nAE = (2.1 × 2.4) / 3.6 = 5.04 / 3.6 = 1.4 cm. [Option (A)]"
      },
      {
        "id": "m_c4_q7",
        "chapterNumber": 4,
        "chapterName": "Geometry",
        "questionNumber": 7,
        "question": "In ΔABC, AD is the internal bisector of ∠BAC. If AB = 8 cm, BD = 6 cm and DC = 3 cm, then the length of AC is",
        "options": [
          {"id": "A", "text": "6 cm"},
          {"id": "B", "text": "4 cm"},
          {"id": "C", "text": "3 cm"},
          {"id": "D", "text": "8 cm"}
        ],
        "correctAnswer": "B",
        "explanation": "By Angle Bisector Theorem:\nAB / AC = BD / DC ⇒ 8 / AC = 6 / 3 = 2\nAC = 8 / 2 = 4 cm. [Option (B)]"
      },
      {
        "id": "m_c4_q8",
        "chapterNumber": 4,
        "chapterName": "Geometry",
        "questionNumber": 8,
        "question": "In right triangle ΔABC, ∠BAC = 90° and AD ⊥ BC. Then",
        "options": [
          {"id": "A", "text": "BD · CD = BC²"},
          {"id": "B", "text": "AB · AC = BC²"},
          {"id": "C", "text": "BD · CD = AD²"},
          {"id": "D", "text": "AB · AC = AD²"}
        ],
        "correctAnswer": "C",
        "explanation": "Since AD ⊥ BC in a right-angled triangle, ΔDBA ~ ΔDAC.\nBD / AD = AD / CD ⇒ BD · CD = AD². [Option (C)]"
      },
      {
        "id": "m_c4_q9",
        "chapterNumber": 4,
        "chapterName": "Geometry",
        "questionNumber": 9,
        "question": "Two poles of heights 6 m and 11 m stand vertically on a ground. If the horizontal distance between them is 12 m, what is the distance between their tops?",
        "options": [
          {"id": "A", "text": "13 m"},
          {"id": "B", "text": "14 m"},
          {"id": "C", "text": "15 m"},
          {"id": "D", "text": "12.8 m"}
        ],
        "correctAnswer": "A",
        "explanation": "Vertical difference in height = 11 - 6 = 5 m.\nHorizontal distance between poles = 12 m.\nDistance between tops = √(12² + 5²) = √(144 + 25) = √169 = 13 m. [Option (A)]"
      },
      {
        "id": "m_c4_q10",
        "chapterNumber": 4,
        "chapterName": "Geometry",
        "questionNumber": 10,
        "question": "In ΔPQR, PR = 26 cm, QR = 24 cm, and in right triangle PAQ, ∠PAQ = 90°, PA = 6 cm, QA = 8 cm. Then ∠PQR is",
        "options": [
          {"id": "A", "text": "80°"},
          {"id": "B", "text": "85°"},
          {"id": "C", "text": "75°"},
          {"id": "D", "text": "90°"}
        ],
        "correctAnswer": "D",
        "explanation": "In ΔPAQ: PQ² = PA² + QA² = 6² + 8² = 36 + 64 = 100 ⇒ PQ = 10 cm.\nIn ΔPQR: PQ² + QR² = 10² + 24² = 100 + 576 = 676 = 26² = PR².\nBy converse of Pythagoras theorem, ΔPQR is right-angled at Q, so ∠PQR = 90°. [Option (D)]"
      },
      {
        "id": "m_c4_q11",
        "chapterNumber": 4,
        "chapterName": "Geometry",
        "questionNumber": 11,
        "question": "For a circle, a tangent is perpendicular to the radius at the",
        "options": [
          {"id": "A", "text": "centre"},
          {"id": "B", "text": "point of contact"},
          {"id": "C", "text": "infinity"},
          {"id": "D", "text": "chord"}
        ],
        "correctAnswer": "B",
        "explanation": "By circle theorem, a tangent to a circle is perpendicular to the radius through the point of contact. [Option (B)]"
      },
      {
        "id": "m_c4_q12",
        "chapterNumber": 4,
        "chapterName": "Geometry",
        "questionNumber": 12,
        "question": "The number of tangents that can be drawn to a circle from an exterior point is",
        "options": [
          {"id": "A", "text": "one"},
          {"id": "B", "text": "two"},
          {"id": "C", "text": "infinite"},
          {"id": "D", "text": "zero"}
        ],
        "correctAnswer": "B",
        "explanation": "From any point lying outside a circle, exactly two distinct tangents can be drawn to the circle. [Option (B)]"
      },
      {
        "id": "m_c4_q13",
        "chapterNumber": 4,
        "chapterName": "Geometry",
        "questionNumber": 13,
        "question": "The two tangents from an external point P to a circle with centre at O are PA and PB. If ∠APB = 70°, then the value of ∠AOB is",
        "options": [
          {"id": "A", "text": "100°"},
          {"id": "B", "text": "110°"},
          {"id": "C", "text": "120°"},
          {"id": "D", "text": "130°"}
        ],
        "correctAnswer": "B",
        "explanation": "OAPB forms a quadrilateral where ∠OAP = ∠OBP = 90°.\nSum of opposite angles ∠APB + ∠AOB = 180° ⇒ ∠AOB = 180° - 70° = 110°. [Option (B)]"
      },
      {
        "id": "m_c4_q14",
        "chapterNumber": 4,
        "chapterName": "Geometry",
        "questionNumber": 14,
        "question": "CP and CQ are tangents to a circle with centre O. ARB is another tangent touching the circle at R. If CP = 11 cm and BC = 7 cm, then the length of BR is",
        "options": [
          {"id": "A", "text": "6 cm"},
          {"id": "B", "text": "5 cm"},
          {"id": "C", "text": "8 cm"},
          {"id": "D", "text": "4 cm"}
        ],
        "correctAnswer": "D",
        "explanation": "Tangents from external point C are equal: CQ = CP = 11 cm.\nBQ = CQ - BC = 11 - 7 = 4 cm.\nSince tangents from external point B are equal, BR = BQ = 4 cm. [Option (D)]"
      },
      {
        "id": "m_c4_q15",
        "chapterNumber": 4,
        "chapterName": "Geometry",
        "questionNumber": 15,
        "question": "If PR is tangent to a circle at P with centre O and ∠OPR = 90°, and ∠QPR = 60°, then ∠POQ is",
        "options": [
          {"id": "A", "text": "120°"},
          {"id": "B", "text": "100°"},
          {"id": "C", "text": "110°"},
          {"id": "D", "text": "90°"}
        ],
        "correctAnswer": "A",
        "explanation": "∠OPQ = ∠OPR - ∠QPR = 90° - 60° = 30°.\nIn isosceles ΔOPQ (OP = OQ = radius), ∠OQP = ∠OPQ = 30°.\n∠POQ = 180° - (30° + 30°) = 120°. [Option (A)]"
      }
    ]
  },

  # -------------------- CHAPTER 5 --------------------
  {
    "chapterNumber": 5,
    "chapterName": "Coordinate Geometry",
    "icon": "fa-chart-line",
    "color": "#e11d48",
    "description": "Area of triangle & quadrilateral, slope of straight line, equations of lines, parallel & perpendicular lines",
    "questions": [
      {
        "id": "m_c5_q1",
        "chapterNumber": 5,
        "chapterName": "Coordinate Geometry",
        "questionNumber": 1,
        "question": "The area of the triangle formed by the points (-5, 0), (0, -5) and (5, 0) is",
        "options": [
          {"id": "A", "text": "0 sq. units"},
          {"id": "B", "text": "25 sq. units"},
          {"id": "C", "text": "5 sq. units"},
          {"id": "D", "text": "None of these"}
        ],
        "correctAnswer": "B",
        "explanation": "Area = (1/2) |x₁(y₂ - y₃) + x₂(y₃ - y₁) + x₃(y₁ - y₂)|\n= (1/2) |(-5)(-5 - 0) + 0(0 - 0) + 5(0 - (-5))|\n= (1/2) |25 + 0 + 25| = (1/2)(50) = 25 sq. units. [Option (B)]"
      },
      {
        "id": "m_c5_q2",
        "chapterNumber": 5,
        "chapterName": "Coordinate Geometry",
        "questionNumber": 2,
        "question": "A man walks parallel to a wall such that the distance between him and the wall is 10 units. Considering the wall as Y-axis, the path travelled by the man is",
        "options": [
          {"id": "A", "text": "x = 10"},
          {"id": "B", "text": "y = 10"},
          {"id": "C", "text": "x = 0"},
          {"id": "D", "text": "y = 0"}
        ],
        "correctAnswer": "A",
        "explanation": "Any line parallel to the Y-axis at a distance of 10 units from it has constant x-coordinate: x = 10. [Option (A)]"
      },
      {
        "id": "m_c5_q3",
        "chapterNumber": 5,
        "chapterName": "Coordinate Geometry",
        "questionNumber": 3,
        "question": "The straight line x = 11 is",
        "options": [
          {"id": "A", "text": "parallel to X-axis"},
          {"id": "B", "text": "parallel to Y-axis"},
          {"id": "C", "text": "passing through the origin"},
          {"id": "D", "text": "passing through (0, 11)"}
        ],
        "correctAnswer": "B",
        "explanation": "An equation of the form x = c is a vertical line, which is parallel to the Y-axis. [Option (B)]"
      },
      {
        "id": "m_c5_q4",
        "chapterNumber": 5,
        "chapterName": "Coordinate Geometry",
        "questionNumber": 4,
        "question": "If (5, 7), (3, p) and (6, 6) are collinear, then the value of p is",
        "options": [
          {"id": "A", "text": "3"},
          {"id": "B", "text": "6"},
          {"id": "C", "text": "9"},
          {"id": "D", "text": "12"}
        ],
        "correctAnswer": "C",
        "explanation": "Since points A(5, 7), B(3, p), C(6, 6) are collinear, Slope(AB) = Slope(BC):\n(p - 7) / (3 - 5) = (6 - p) / (6 - 3)\n(p - 7) / (-2) = (6 - p) / 3 ⇒ 3(p - 7) = -2(6 - p)\n3p - 21 = -12 + 2p ⇒ p = 9. [Option (C)]"
      },
      {
        "id": "m_c5_q5",
        "chapterNumber": 5,
        "chapterName": "Coordinate Geometry",
        "questionNumber": 5,
        "question": "The point of intersection of 3x - y = 4 and x + y = 8 is",
        "options": [
          {"id": "A", "text": "(5, 3)"},
          {"id": "B", "text": "(2, 4)"},
          {"id": "C", "text": "(3, 5)"},
          {"id": "D", "text": "(4, 4)"}
        ],
        "correctAnswer": "C",
        "explanation": "Adding both equations: (3x - y) + (x + y) = 4 + 8 ⇒ 4x = 12 ⇒ x = 3.\nSubstituting x = 3 into x + y = 8 gives 3 + y = 8 ⇒ y = 5.\nPoint of intersection is (3, 5). [Option (C)]"
      },
      {
        "id": "m_c5_q6",
        "chapterNumber": 5,
        "chapterName": "Coordinate Geometry",
        "questionNumber": 6,
        "question": "If the slope of the line joining (12, 3) and (4, a) is 1/8, then the value of 'a' is",
        "options": [
          {"id": "A", "text": "1"},
          {"id": "B", "text": "4"},
          {"id": "C", "text": "-5"},
          {"id": "D", "text": "2"}
        ],
        "correctAnswer": "D",
        "explanation": "Slope m = (a - 3) / (4 - 12) = (a - 3) / (-8).\nGiven m = 1/8 ⇒ (a - 3) / (-8) = 1/8 ⇒ a - 3 = -1 ⇒ a = 2. [Option (D)]"
      },
      {
        "id": "m_c5_q7",
        "chapterNumber": 5,
        "chapterName": "Coordinate Geometry",
        "questionNumber": 7,
        "question": "The slope of the line which is perpendicular to the line joining the points (0, 0) and (-8, 8) is",
        "options": [
          {"id": "A", "text": "-1"},
          {"id": "B", "text": "1"},
          {"id": "C", "text": "1/3"},
          {"id": "D", "text": "-8"}
        ],
        "correctAnswer": "B",
        "explanation": "Slope of line m₁ = (8 - 0) / (-8 - 0) = 8 / (-8) = -1.\nSlope of perpendicular line m₂ = -1 / m₁ = -1 / (-1) = 1. [Option (B)]"
      },
      {
        "id": "m_c5_q8",
        "chapterNumber": 5,
        "chapterName": "Coordinate Geometry",
        "questionNumber": 8,
        "question": "If the slope of a line is -1/√3, then the slope of the perpendicular bisector of the line is",
        "options": [
          {"id": "A", "text": "-√3"},
          {"id": "B", "text": "√3"},
          {"id": "C", "text": "1/√3"},
          {"id": "D", "text": "0"}
        ],
        "correctAnswer": "B",
        "explanation": "For perpendicular lines, m₁ × m₂ = -1.\n(-1/√3) × m₂ = -1 ⇒ m₂ = √3. [Option (B)]"
      },
      {
        "id": "m_c5_q9",
        "chapterNumber": 5,
        "chapterName": "Coordinate Geometry",
        "questionNumber": 9,
        "question": "If A is a point on the Y-axis whose ordinate is 8 and B is a point on the X-axis whose abscissa is 5, then the equation of the line AB is",
        "options": [
          {"id": "A", "text": "8x + 5y = 40"},
          {"id": "B", "text": "8x - 5y = 40"},
          {"id": "C", "text": "x = 8"},
          {"id": "D", "text": "y = 5"}
        ],
        "correctAnswer": "A",
        "explanation": "X-intercept a = 5, Y-intercept b = 8.\nIntercept form: x/a + y/b = 1 ⇒ x/5 + y/8 = 1 ⇒ 8x + 5y = 40. [Option (A)]"
      },
      {
        "id": "m_c5_q10",
        "chapterNumber": 5,
        "chapterName": "Coordinate Geometry",
        "questionNumber": 10,
        "question": "The equation of a line passing through the origin and perpendicular to the line 7x - 3y + 4 = 0 is",
        "options": [
          {"id": "A", "text": "7x - 3y + 4 = 0"},
          {"id": "B", "text": "3x - 7y + 4 = 0"},
          {"id": "C", "text": "3x + 7y = 0"},
          {"id": "D", "text": "7x - 3y = 0"}
        ],
        "correctAnswer": "C",
        "explanation": "Any line perpendicular to ax + by + c = 0 is of the form bx - ay + k = 0.\nHere 7x - 3y + 4 = 0 becomes 3x + 7y + k = 0.\nSince it passes through origin (0, 0): 3(0) + 7(0) + k = 0 ⇒ k = 0.\nEquation is 3x + 7y = 0. [Option (C)]"
      },
      {
        "id": "m_c5_q11",
        "chapterNumber": 5,
        "chapterName": "Coordinate Geometry",
        "questionNumber": 11,
        "question": "Consider four lines: l₁: 3y = 4x + 5, l₂: 4y = 3x - 1, l₃: 4y + 3x = 7, l₄: 4x + 3y = 2. Which of the following statement is true?",
        "options": [
          {"id": "A", "text": "l₁ and l₂ are perpendicular"},
          {"id": "B", "text": "l₁ and l₄ are parallel"},
          {"id": "C", "text": "l₂ and l₄ are perpendicular"},
          {"id": "D", "text": "l₂ and l₃ are parallel"}
        ],
        "correctAnswer": "C",
        "explanation": "Slope of l₂: m₂ = 3/4.\nSlope of l₄: 3y = -4x + 2 ⇒ m₄ = -4/3.\nProduct of slopes: m₂ × m₄ = (3/4) × (-4/3) = -1.\nHence l₂ and l₄ are perpendicular. [Option (C)]"
      },
      {
        "id": "m_c5_q12",
        "chapterNumber": 5,
        "chapterName": "Coordinate Geometry",
        "questionNumber": 12,
        "question": "For the straight line equation 8y = 4x + 21, which of the following is true?",
        "options": [
          {"id": "A", "text": "The slope is 0.5 and the y-intercept is 2.6"},
          {"id": "B", "text": "The slope is 5 and the y-intercept is 1.6"},
          {"id": "C", "text": "The slope is 0.5 and the y-intercept is 1.6"},
          {"id": "D", "text": "The slope is 5 and y-intercept is 2.6"}
        ],
        "correctAnswer": "A",
        "explanation": "Rearranging into y = mx + c: y = (4/8)x + (21/8) = 0.5x + 2.625.\nSlope m = 0.5 and y-intercept ≈ 2.6. [Option (A)]"
      },
      {
        "id": "m_c5_q13",
        "chapterNumber": 5,
        "chapterName": "Coordinate Geometry",
        "questionNumber": 13,
        "question": "When proving that a quadrilateral is a trapezium, it is necessary to show that",
        "options": [
          {"id": "A", "text": "Two pairs of opposite sides are parallel"},
          {"id": "B", "text": "One pair of opposite sides are parallel"},
          {"id": "C", "text": "Opposite sides are parallel and equal"},
          {"id": "D", "text": "All sides are of equal length"}
        ],
        "correctAnswer": "B",
        "explanation": "By definition, a trapezium is a quadrilateral in which exactly one pair of opposite sides is parallel. [Option (B)]"
      },
      {
        "id": "m_c5_q14",
        "chapterNumber": 5,
        "chapterName": "Coordinate Geometry",
        "questionNumber": 14,
        "question": "When proving that a quadrilateral is a parallelogram by using slopes, you must find",
        "options": [
          {"id": "A", "text": "the slopes of two sides"},
          {"id": "B", "text": "the slopes of two pairs of opposite sides"},
          {"id": "C", "text": "the lengths of any two sides"},
          {"id": "D", "text": "both lengths and slopes of two sides"}
        ],
        "correctAnswer": "B",
        "explanation": "A parallelogram has both pairs of opposite sides parallel; hence, we must find and verify equality of slopes for both pairs of opposite sides. [Option (B)]"
      },
      {
        "id": "m_c5_q15",
        "chapterNumber": 5,
        "chapterName": "Coordinate Geometry",
        "questionNumber": 15,
        "question": "(2, 1) is the point of intersection of two lines",
        "options": [
          {"id": "A", "text": "x - y - 3 = 0; 3x - y - 7 = 0"},
          {"id": "B", "text": "x + y = 3; 3x + y = 7"},
          {"id": "C", "text": "3x + y = 3; x + y = 7"},
          {"id": "D", "text": "x + 3y - 3 = 0; x - y - 7 = 0"}
        ],
        "correctAnswer": "B",
        "explanation": "Substituting (2, 1) into Option B:\n2 + 1 = 3 (True)\n3(2) + 1 = 7 (True)\nBoth equations are satisfied by (2, 1). [Option (B)]"
      }
    ]
  },

  # -------------------- CHAPTER 6 --------------------
  {
    "chapterNumber": 6,
    "chapterName": "Trigonometry",
    "icon": "fa-mountain",
    "color": "#8b5cf6",
    "description": "Trigonometric identities, heights and distances, angles of elevation and depression",
    "questions": [
      {
        "id": "m_c6_q1",
        "chapterNumber": 6,
        "chapterName": "Trigonometry",
        "questionNumber": 1,
        "question": "sin² θ + 1 / (1 + tan² θ) is equal to",
        "options": [
          {"id": "A", "text": "tan² θ"},
          {"id": "B", "text": "1"},
          {"id": "C", "text": "cot² θ"},
          {"id": "D", "text": "0"}
        ],
        "correctAnswer": "B",
        "explanation": "1 + tan² θ = sec² θ ⇒ 1 / (1 + tan² θ) = 1 / sec² θ = cos² θ.\nTherefore, sin² θ + cos² θ = 1. [Option (B)]"
      },
      {
        "id": "m_c6_q2",
        "chapterNumber": 6,
        "chapterName": "Trigonometry",
        "questionNumber": 2,
        "question": "tan θ cosec² θ - tan θ is equal to",
        "options": [
          {"id": "A", "text": "sec θ"},
          {"id": "B", "text": "cot² θ"},
          {"id": "C", "text": "sin θ"},
          {"id": "D", "text": "cot θ"}
        ],
        "correctAnswer": "D",
        "explanation": "tan θ (cosec² θ - 1) = tan θ × cot² θ = (tan θ × cot θ) × cot θ = 1 × cot θ = cot θ. [Option (D)]"
      },
      {
        "id": "m_c6_q3",
        "chapterNumber": 6,
        "chapterName": "Trigonometry",
        "questionNumber": 3,
        "question": "If (sin α + cosec α)² + (cos α + sec α)² = k + tan² α + cot² α, then the value of k is equal to",
        "options": [
          {"id": "A", "text": "9"},
          {"id": "B", "text": "7"},
          {"id": "C", "text": "5"},
          {"id": "D", "text": "3"}
        ],
        "correctAnswer": "B",
        "explanation": "Expanding both squares:\n= (sin² α + cos² α) + cosec² α + sec² α + 2 sin α cosec α + 2 cos α sec α\n= 1 + (1 + cot² α) + (1 + tan² α) + 2(1) + 2(1)\n= 1 + 1 + 1 + 2 + 2 + tan² α + cot² α = 7 + tan² α + cot² α ⇒ k = 7. [Option (B)]"
      },
      {
        "id": "m_c6_q4",
        "chapterNumber": 6,
        "chapterName": "Trigonometry",
        "questionNumber": 4,
        "question": "If sin θ + cos θ = a and sec θ + cosec θ = b, then the value of b(a² - 1) is equal to",
        "options": [
          {"id": "A", "text": "2a"},
          {"id": "B", "text": "3a"},
          {"id": "C", "text": "0"},
          {"id": "D", "text": "2ab"}
        ],
        "correctAnswer": "A",
        "explanation": "a² - 1 = (sin θ + cos θ)² - 1 = sin² θ + cos² θ + 2 sin θ cos θ - 1 = 2 sin θ cos θ.\nb = sec θ + cosec θ = (1 / cos θ) + (1 / sin θ) = (sin θ + cos θ) / (sin θ cos θ).\nb(a² - 1) = [(sin θ + cos θ) / (sin θ cos θ)] × 2 sin θ cos θ = 2(sin θ + cos θ) = 2a. [Option (A)]"
      },
      {
        "id": "m_c6_q5",
        "chapterNumber": 6,
        "chapterName": "Trigonometry",
        "questionNumber": 5,
        "question": "If 5x = sec θ and 5/x = tan θ, then x² - 1/x² is equal to",
        "options": [
          {"id": "A", "text": "25"},
          {"id": "B", "text": "1/25"},
          {"id": "C", "text": "5"},
          {"id": "D", "text": "1"}
        ],
        "correctAnswer": "B",
        "explanation": "x = sec θ / 5 and 1/x = tan θ / 5.\nx² - 1/x² = (sec² θ / 25) - (tan² θ / 25) = (sec² θ - tan² θ) / 25 = 1/25. [Option (B)]"
      },
      {
        "id": "m_c6_q6",
        "chapterNumber": 6,
        "chapterName": "Trigonometry",
        "questionNumber": 6,
        "question": "If sin θ = cos θ, then 2 tan² θ + sin² θ - 1 is equal to",
        "options": [
          {"id": "A", "text": "-3/2"},
          {"id": "B", "text": "3/2"},
          {"id": "C", "text": "2/3"},
          {"id": "D", "text": "-2/3"}
        ],
        "correctAnswer": "B",
        "explanation": "sin θ = cos θ ⇒ tan θ = 1 ⇒ θ = 45°.\nsin 45° = 1/√2, so sin² 45° = 1/2.\n2 tan² 45° + sin² 45° - 1 = 2(1)² + 1/2 - 1 = 2 + 1/2 - 1 = 3/2. [Option (B)]"
      },
      {
        "id": "m_c6_q7",
        "chapterNumber": 6,
        "chapterName": "Trigonometry",
        "questionNumber": 7,
        "question": "If x = a tan θ and y = b sec θ, then which of the following holds?",
        "options": [
          {"id": "A", "text": "y²/b² - x²/a² = 1"},
          {"id": "B", "text": "x²/a² - y²/b² = 1"},
          {"id": "C", "text": "x²/a² + y²/b² = 1"},
          {"id": "D", "text": "y²/a² - x²/b² = 1"}
        ],
        "correctAnswer": "A",
        "explanation": "tan θ = x/a and sec θ = y/b.\nSince sec² θ - tan² θ = 1, substituting gives (y/b)² - (x/a)² = 1 ⇒ y²/b² - x²/a² = 1. [Option (A)]"
      },
      {
        "id": "m_c6_q8",
        "chapterNumber": 6,
        "chapterName": "Trigonometry",
        "questionNumber": 8,
        "question": "(1 + tan θ + sec θ)(1 + cot θ - cosec θ) is equal to",
        "options": [
          {"id": "A", "text": "0"},
          {"id": "B", "text": "1"},
          {"id": "C", "text": "2"},
          {"id": "D", "text": "-1"}
        ],
        "correctAnswer": "C",
        "explanation": "Converting to sin and cos:\n[ (cos θ + sin θ + 1) / cos θ ] × [ (sin θ + cos θ - 1) / sin θ ]\n= [ (sin θ + cos θ)² - 1² ] / (sin θ cos θ)\n= [ 1 + 2 sin θ cos θ - 1 ] / (sin θ cos θ) = 2. [Option (C)]"
      },
      {
        "id": "m_c6_q9",
        "chapterNumber": 6,
        "chapterName": "Trigonometry",
        "questionNumber": 9,
        "question": "If a cot θ + b cosec θ = p and b cot θ + a cosec θ = q, then p² - q² is equal to",
        "options": [
          {"id": "A", "text": "a² - b²"},
          {"id": "B", "text": "b² - a²"},
          {"id": "C", "text": "a² + b²"},
          {"id": "D", "text": "b - a"}
        ],
        "correctAnswer": "B",
        "explanation": "p² - q² = (a cot θ + b cosec θ)² - (b cot θ + a cosec θ)²\n= (b² - a²)(cosec² θ - cot² θ) = (b² - a²)(1) = b² - a². [Option (B)]"
      },
      {
        "id": "m_c6_q10",
        "chapterNumber": 6,
        "chapterName": "Trigonometry",
        "questionNumber": 10,
        "question": "If the ratio of the height of a tower and the length of its shadow is √3 : 1, then the angle of elevation of the sun is",
        "options": [
          {"id": "A", "text": "45°"},
          {"id": "B", "text": "30°"},
          {"id": "C", "text": "90°"},
          {"id": "D", "text": "60°"}
        ],
        "correctAnswer": "D",
        "explanation": "tan θ = Height / Shadow = √3 / 1 = √3.\nSince tan 60° = √3, angle of elevation θ = 60°. [Option (D)]"
      },
      {
        "id": "m_c6_q11",
        "chapterNumber": 6,
        "chapterName": "Trigonometry",
        "questionNumber": 11,
        "question": "An electric pole subtends an angle of depression 30° at a point B on the same level as its foot. At another point 'b' metres above B, the depression of the foot of the pole is 60°. The height of the tower (in metres) is equal to",
        "options": [
          {"id": "A", "text": "√3 b"},
          {"id": "B", "text": "b / 3"},
          {"id": "C", "text": "b / 2"},
          {"id": "D", "text": "b / √3"}
        ],
        "correctAnswer": "B",
        "explanation": "Let distance between the two verticals be d.\ntan 60° = b / d ⇒ d = b / √3.\ntan 30° = h / d ⇒ h = d × tan 30° = (b / √3) × (1 / √3) = b / 3. [Option (B)]"
      },
      {
        "id": "m_c6_q12",
        "chapterNumber": 6,
        "chapterName": "Trigonometry",
        "questionNumber": 12,
        "question": "A tower is 60 m high. Its shadow reduces by x metres when the angle of elevation of the sun increases from 30° to 45°. Then x is equal to",
        "options": [
          {"id": "A", "text": "41.92 m"},
          {"id": "B", "text": "43.92 m"},
          {"id": "C", "text": "43 m"},
          {"id": "D", "text": "45.6 m"}
        ],
        "correctAnswer": "B",
        "explanation": "At 45°: shadow length = 60 / tan 45° = 60 m.\nAt 30°: shadow length = 60 / tan 30° = 60√3 m.\nReduction x = 60√3 - 60 = 60(√3 - 1) = 60(1.732 - 1) = 60(0.732) = 43.92 m. [Option (B)]"
      },
      {
        "id": "m_c6_q13",
        "chapterNumber": 6,
        "chapterName": "Trigonometry",
        "questionNumber": 13,
        "question": "The angles of depression of the top and bottom of a 20 m tall building from the top of a multistoried building are 30° and 60° respectively. The height of the multistoried building and the distance between the two buildings (in metres) are",
        "options": [
          {"id": "A", "text": "20 m, 10√3 m"},
          {"id": "B", "text": "30 m, 5√3 m"},
          {"id": "C", "text": "20 m, 10 m"},
          {"id": "D", "text": "30 m, 10√3 m"}
        ],
        "correctAnswer": "D",
        "explanation": "Let total height be H = x + 20 and distance be d.\ntan 30° = x / d ⇒ d = x√3.\ntan 60° = (x + 20) / d ⇒ √3 = (x + 20) / (x√3) ⇒ 3x = x + 20 ⇒ x = 10 m.\nTotal height = 10 + 20 = 30 m.\nDistance d = 10√3 m. [Option (D)]"
      },
      {
        "id": "m_c6_q14",
        "chapterNumber": 6,
        "chapterName": "Trigonometry",
        "questionNumber": 14,
        "question": "Two persons are standing 'x' metres apart and the height of one is double that of the other. If from the midpoint of the line joining their feet, an observer finds the angular elevations of their tops to be complementary, then the height of the shorter person (in metres) is",
        "options": [
          {"id": "A", "text": "√2 x"},
          {"id": "B", "text": "x / (2√2)"},
          {"id": "C", "text": "x / √2"},
          {"id": "D", "text": "2x"}
        ],
        "correctAnswer": "B",
        "explanation": "Let height of shorter person be h, taller person 2h. Distance from midpoint to each person = x/2.\nSince elevations are complementary (θ and 90° - θ):\ntan θ = 2h / (x/2) = 4h / x.\ntan(90° - θ) = cot θ = h / (x/2) = 2h / x.\ntan θ × cot θ = 1 ⇒ (4h / x) × (2h / x) = 1 ⇒ 8h² / x² = 1 ⇒ h² = x² / 8\n⇒ h = x / √8 = x / (2√2) m. [Option (B)]"
      },
      {
        "id": "m_c6_q15",
        "chapterNumber": 6,
        "chapterName": "Trigonometry",
        "questionNumber": 15,
        "question": "The angle of elevation of a cloud from a point h metres above a lake is θ. The angle of depression of its reflection in the lake is 45°. The height of the cloud from the surface of the lake is",
        "options": [
          {"id": "A", "text": "h(1 + tan θ) / (1 - tan θ)"},
          {"id": "B", "text": "h(1 - tan θ) / (1 + tan θ)"},
          {"id": "C", "text": "h tan(45° - θ)"},
          {"id": "D", "text": "None of these"}
        ],
        "correctAnswer": "A",
        "explanation": "Let height of cloud above lake be H. Cloud is (H - h) above observation point, reflection is (H + h) below.\ntan θ = (H - h) / d and tan 45° = (H + h) / d = 1 ⇒ d = H + h.\nThus tan θ = (H - h) / (H + h) ⇒ H tan θ + h tan θ = H - h\n⇒ H(1 - tan θ) = h(1 + tan θ) ⇒ H = h(1 + tan θ) / (1 - tan θ). [Option (A)]"
      }
    ]
  },

  # -------------------- CHAPTER 7 --------------------
  {
    "chapterNumber": 7,
    "chapterName": "Mensuration",
    "icon": "fa-cube",
    "color": "#0ea5e9",
    "description": "Surface area and volume of cylinder, cone, sphere, hemisphere, frustum, and combination of solids",
    "questions": [
      {
        "id": "m_c7_q1",
        "chapterNumber": 7,
        "chapterName": "Mensuration",
        "questionNumber": 1,
        "question": "The curved surface area of a right circular cone of height 15 cm and base diameter 16 cm is",
        "options": [
          {"id": "A", "text": "60π cm²"},
          {"id": "B", "text": "68π cm²"},
          {"id": "C", "text": "120π cm²"},
          {"id": "D", "text": "136π cm²"}
        ],
        "correctAnswer": "D",
        "explanation": "Radius r = 16 / 2 = 8 cm, height h = 15 cm.\nSlant height l = √(h² + r²) = √(15² + 8²) = √(225 + 64) = √289 = 17 cm.\nCSA = π r l = π × 8 × 17 = 136π cm². [Option (D)]"
      },
      {
        "id": "m_c7_q2",
        "chapterNumber": 7,
        "chapterName": "Mensuration",
        "questionNumber": 2,
        "question": "If two solid hemispheres of same base radius r units are joined together along their bases, then curved surface area of this new solid is",
        "options": [
          {"id": "A", "text": "4πr² sq. units"},
          {"id": "B", "text": "6πr² sq. units"},
          {"id": "C", "text": "3πr² sq. units"},
          {"id": "D", "text": "8πr² sq. units"}
        ],
        "correctAnswer": "A",
        "explanation": "Joining two solid hemispheres along their bases forms a complete solid sphere of radius r.\nThe surface area of a sphere of radius r is 4πr² sq. units. [Option (A)]"
      },
      {
        "id": "m_c7_q3",
        "chapterNumber": 7,
        "chapterName": "Mensuration",
        "questionNumber": 3,
        "question": "The height of a right circular cone whose radius is 5 cm and slant height is 13 cm is",
        "options": [
          {"id": "A", "text": "12 cm"},
          {"id": "B", "text": "10 cm"},
          {"id": "C", "text": "13 cm"},
          {"id": "D", "text": "5 cm"}
        ],
        "correctAnswer": "A",
        "explanation": "h = √(l² - r²) = √(13² - 5²) = √(169 - 25) = √144 = 12 cm. [Option (A)]"
      },
      {
        "id": "m_c7_q4",
        "chapterNumber": 7,
        "chapterName": "Mensuration",
        "questionNumber": 4,
        "question": "If the radius of the base of a right circular cylinder is halved keeping the same height, then the ratio of the volume of the new cylinder to the original cylinder is",
        "options": [
          {"id": "A", "text": "1 : 2"},
          {"id": "B", "text": "1 : 4"},
          {"id": "C", "text": "1 : 6"},
          {"id": "D", "text": "1 : 8"}
        ],
        "correctAnswer": "B",
        "explanation": "Original volume = π r² h.\nNew volume = π (r/2)² h = π (r²/4) h = (1/4) π r² h.\nRatio = [(1/4) π r² h] / [π r² h] = 1 : 4. [Option (B)]"
      },
      {
        "id": "m_c7_q5",
        "chapterNumber": 7,
        "chapterName": "Mensuration",
        "questionNumber": 5,
        "question": "The total surface area of a cylinder whose radius is 1/3 of its height h is",
        "options": [
          {"id": "A", "text": "9/8 πh² sq. units"},
          {"id": "B", "text": "24πh² sq. units"},
          {"id": "C", "text": "8/9 πh² sq. units"},
          {"id": "D", "text": "56/9 πh² sq. units"}
        ],
        "correctAnswer": "C",
        "explanation": "TSA = 2πr(h + r) with r = h/3:\n= 2π(h/3)[h + h/3] = 2π(h/3)(4h/3) = (8/9) πh² sq. units. [Option (C)]"
      },
      {
        "id": "m_c7_q6",
        "chapterNumber": 7,
        "chapterName": "Mensuration",
        "questionNumber": 6,
        "question": "In a hollow cylinder, the sum of the external and internal radii is 14 cm and the width is 4 cm. If its height is 20 cm, the volume of the material is",
        "options": [
          {"id": "A", "text": "5600π cm³"},
          {"id": "B", "text": "1120π cm³"},
          {"id": "C", "text": "56π cm³"},
          {"id": "D", "text": "3600π cm³"}
        ],
        "correctAnswer": "B",
        "explanation": "R + r = 14 cm, width = R - r = 4 cm, h = 20 cm.\nVolume = π h (R² - r²) = π h (R + r)(R - r) = π × 20 × 14 × 4 = 1120π cm³. [Option (B)]"
      },
      {
        "id": "m_c7_q7",
        "chapterNumber": 7,
        "chapterName": "Mensuration",
        "questionNumber": 7,
        "question": "If the radius of the base of a cone is tripled and the height is doubled, then the volume increases",
        "options": [
          {"id": "A", "text": "6 times"},
          {"id": "B", "text": "18 times"},
          {"id": "C", "text": "12 times"},
          {"id": "D", "text": "unchanged"}
        ],
        "correctAnswer": "B",
        "explanation": "Original volume V₁ = (1/3) π r² h.\nNew volume V₂ = (1/3) π (3r)² (2h) = (1/3) π (9r²) (2h) = 18 × [(1/3) π r² h] = 18 V₁.\nVolume increases 18 times. [Option (B)]"
      },
      {
        "id": "m_c7_q8",
        "chapterNumber": 7,
        "chapterName": "Mensuration",
        "questionNumber": 8,
        "question": "The total surface area of a hemisphere is how many times the square of its radius?",
        "options": [
          {"id": "A", "text": "π"},
          {"id": "B", "text": "4π"},
          {"id": "C", "text": "3π"},
          {"id": "D", "text": "2π"}
        ],
        "correctAnswer": "C",
        "explanation": "TSA of a solid hemisphere = 3π r² = 3π × (r²).\nHence it is 3π times the square of its radius. [Option (C)]"
      },
      {
        "id": "m_c7_q9",
        "chapterNumber": 7,
        "chapterName": "Mensuration",
        "questionNumber": 9,
        "question": "A solid sphere of radius x cm is melted and cast into the shape of a solid cone of same radius. The height of the cone is",
        "options": [
          {"id": "A", "text": "3x cm"},
          {"id": "B", "text": "x cm"},
          {"id": "C", "text": "4x cm"},
          {"id": "D", "text": "2x cm"}
        ],
        "correctAnswer": "C",
        "explanation": "Volume of cone = Volume of sphere\n(1/3) π x² h = (4/3) π x³ ⇒ h = 4x cm. [Option (C)]"
      },
      {
        "id": "m_c7_q10",
        "chapterNumber": 7,
        "chapterName": "Mensuration",
        "questionNumber": 10,
        "question": "A frustum of a right circular cone is of height 16 cm with radii of its ends as 8 cm and 20 cm. Then the volume of the frustum is",
        "options": [
          {"id": "A", "text": "3328π cm³"},
          {"id": "B", "text": "3228π cm³"},
          {"id": "C", "text": "3240π cm³"},
          {"id": "D", "text": "3340π cm³"}
        ],
        "correctAnswer": "A",
        "explanation": "Volume of frustum = (1/3) π h (R² + r² + R r)\n= (1/3) π × 16 × [20² + 8² + (20)(8)]\n= (1/3) π × 16 × [400 + 64 + 160] = (1/3) π × 16 × 624 = 16 × 208 π = 3328π cm³. [Option (A)]"
      },
      {
        "id": "m_c7_q11",
        "chapterNumber": 7,
        "chapterName": "Mensuration",
        "questionNumber": 11,
        "question": "A shuttlecock used for playing badminton has the shape of the combination of",
        "options": [
          {"id": "A", "text": "a cylinder and a sphere"},
          {"id": "B", "text": "a hemisphere and a cone"},
          {"id": "C", "text": "a sphere and a cone"},
          {"id": "D", "text": "frustum of a cone and a hemisphere"}
        ],
        "correctAnswer": "D",
        "explanation": "A badminton shuttlecock consists of a rounded cork base (hemisphere) and an open skirt of feathers (frustum of a cone). [Option (D)]"
      },
      {
        "id": "m_c7_q12",
        "chapterNumber": 7,
        "chapterName": "Mensuration",
        "questionNumber": 12,
        "question": "A spherical ball of radius r₁ units is melted to make 8 identical balls each of radius r₂ units. Then r₁ : r₂ is",
        "options": [
          {"id": "A", "text": "2 : 1"},
          {"id": "B", "text": "1 : 2"},
          {"id": "C", "text": "4 : 1"},
          {"id": "D", "text": "1 : 4"}
        ],
        "correctAnswer": "A",
        "explanation": "Volume of large sphere = 8 × Volume of small sphere\n(4/3) π r₁³ = 8 × (4/3) π r₂³ ⇒ r₁³ = 8 r₂³ ⇒ (r₁ / r₂)³ = 8 ⇒ r₁ / r₂ = 2 / 1 = 2 : 1. [Option (A)]"
      },
      {
        "id": "m_c7_q13",
        "chapterNumber": 7,
        "chapterName": "Mensuration",
        "questionNumber": 13,
        "question": "The volume (in cm³) of the greatest sphere that can be cut off from a cylindrical log of wood of base radius 1 cm and height 5 cm is",
        "options": [
          {"id": "A", "text": "4/3 π"},
          {"id": "B", "text": "10/3 π"},
          {"id": "C", "text": "5π"},
          {"id": "D", "text": "20/3 π"}
        ],
        "correctAnswer": "A",
        "explanation": "The maximum diameter of the sphere is limited by the diameter of the cylinder (2 × 1 = 2 cm), so maximum radius of the sphere is r = 1 cm.\nVolume = (4/3) π r³ = (4/3) π (1)³ = (4/3) π cm³. [Option (A)]"
      },
      {
        "id": "m_c7_q14",
        "chapterNumber": 7,
        "chapterName": "Mensuration",
        "questionNumber": 14,
        "question": "The height and radius of the cone of which the frustum is a part are h₁ units and r₁ units respectively. Height of the frustum is h₂ units and radius of smaller base is r₂ units. If h₂ : h₁ = 1 : 2, then r₂ : r₁ is",
        "options": [
          {"id": "A", "text": "1 : 3"},
          {"id": "B", "text": "1 : 2"},
          {"id": "C", "text": "2 : 1"},
          {"id": "D", "text": "3 : 1"}
        ],
        "correctAnswer": "B",
        "explanation": "By similar triangles in the cross-section:\n(h₁ - h₂) / h₁ = r₂ / r₁ ⇒ 1 - (h₂ / h₁) = r₂ / r₁\nSince h₂ : h₁ = 1 : 2, 1 - 1/2 = 1/2 = r₂ / r₁ ⇒ r₂ : r₁ = 1 : 2. [Option (B)]"
      },
      {
        "id": "m_c7_q15",
        "chapterNumber": 7,
        "chapterName": "Mensuration",
        "questionNumber": 15,
        "question": "The ratio of the volumes of a cylinder, a cone and a sphere, if each has the same diameter and same height (height = 2r) is",
        "options": [
          {"id": "A", "text": "1 : 2 : 3"},
          {"id": "B", "text": "2 : 1 : 3"},
          {"id": "C", "text": "1 : 3 : 2"},
          {"id": "D", "text": "3 : 1 : 2"}
        ],
        "correctAnswer": "D",
        "explanation": "Height h = 2r.\nV(cylinder) = π r² (2r) = 2πr³.\nV(cone) = (1/3) π r² (2r) = (2/3) πr³.\nV(sphere) = (4/3) πr³.\nRatio = 2 : (2/3) : (4/3) = 6 : 2 : 4 = 3 : 1 : 2. [Option (D)]"
      }
    ]
  },

  # -------------------- CHAPTER 8 --------------------
  {
    "chapterNumber": 8,
    "chapterName": "Statistics and Probability",
    "icon": "fa-chart-pie",
    "color": "#0d9488",
    "description": "Measures of dispersion (range, SD, variance), coefficient of variation, probability of events, addition theorem",
    "questions": [
      {
        "id": "m_c8_q1",
        "chapterNumber": 8,
        "chapterName": "Statistics and Probability",
        "questionNumber": 1,
        "question": "Which of the following is not a measure of dispersion?",
        "options": [
          {"id": "A", "text": "Range"},
          {"id": "B", "text": "Standard deviation"},
          {"id": "C", "text": "Arithmetic mean"},
          {"id": "D", "text": "Variance"}
        ],
        "correctAnswer": "C",
        "explanation": "Arithmetic mean is a measure of central tendency, whereas Range, Standard deviation, and Variance are measures of dispersion. [Option (C)]"
      },
      {
        "id": "m_c8_q2",
        "chapterNumber": 8,
        "chapterName": "Statistics and Probability",
        "questionNumber": 2,
        "question": "The range of the data 8, 8, 8, 8, 8, ..., 8 is",
        "options": [
          {"id": "A", "text": "0"},
          {"id": "B", "text": "1"},
          {"id": "C", "text": "8"},
          {"id": "D", "text": "3"}
        ],
        "correctAnswer": "A",
        "explanation": "Range = Largest value (L) - Smallest value (S) = 8 - 8 = 0. [Option (A)]"
      },
      {
        "id": "m_c8_q3",
        "chapterNumber": 8,
        "chapterName": "Statistics and Probability",
        "questionNumber": 3,
        "question": "The sum of all deviations of the data from its mean is",
        "options": [
          {"id": "A", "text": "Always positive"},
          {"id": "B", "text": "Always negative"},
          {"id": "C", "text": "zero"},
          {"id": "D", "text": "non-zero integer"}
        ],
        "correctAnswer": "C",
        "explanation": "By the algebraic property of the arithmetic mean: Σ(xᵢ - x̄) = Σxᵢ - n x̄ = n x̄ - n x̄ = 0. [Option (C)]"
      },
      {
        "id": "m_c8_q4",
        "chapterNumber": 8,
        "chapterName": "Statistics and Probability",
        "questionNumber": 4,
        "question": "The mean of 100 observations is 40 and their standard deviation is 3. The sum of squares of all observations is",
        "options": [
          {"id": "A", "text": "40000"},
          {"id": "B", "text": "160900"},
          {"id": "C", "text": "160000"},
          {"id": "D", "text": "30000"}
        ],
        "correctAnswer": "B",
        "explanation": "σ² = (Σx² / n) - (x̄)² ⇒ 3² = (Σx² / 100) - 40²\n9 = (Σx² / 100) - 1600 ⇒ Σx² / 100 = 1609 ⇒ Σx² = 160900. [Option (B)]"
      },
      {
        "id": "m_c8_q5",
        "chapterNumber": 8,
        "chapterName": "Statistics and Probability",
        "questionNumber": 5,
        "question": "Variance of first 20 natural numbers is",
        "options": [
          {"id": "A", "text": "32.25"},
          {"id": "B", "text": "44.25"},
          {"id": "C", "text": "33.25"},
          {"id": "D", "text": "30"}
        ],
        "correctAnswer": "C",
        "explanation": "Variance of first n natural numbers = (n² - 1) / 12.\nFor n = 20: (20² - 1) / 12 = (400 - 1) / 12 = 399 / 12 = 33.25. [Option (C)]"
      },
      {
        "id": "m_c8_q6",
        "chapterNumber": 8,
        "chapterName": "Statistics and Probability",
        "questionNumber": 6,
        "question": "The standard deviation of a data is 3. If each value is multiplied by 5, then the new variance is",
        "options": [
          {"id": "A", "text": "3"},
          {"id": "B", "text": "15"},
          {"id": "C", "text": "5"},
          {"id": "D", "text": "225"}
        ],
        "correctAnswer": "D",
        "explanation": "If each observation is multiplied by k = 5, the new standard deviation becomes k × σ = 5 × 3 = 15.\nNew Variance = (new σ)² = 15² = 225. [Option (D)]"
      },
      {
        "id": "m_c8_q7",
        "chapterNumber": 8,
        "chapterName": "Statistics and Probability",
        "questionNumber": 7,
        "question": "If the standard deviation of x, y, z is p, then the standard deviation of 3x + 5, 3y + 5, 3z + 5 is",
        "options": [
          {"id": "A", "text": "3p + 5"},
          {"id": "B", "text": "3p"},
          {"id": "C", "text": "p + 5"},
          {"id": "D", "text": "9p + 15"}
        ],
        "correctAnswer": "B",
        "explanation": "Adding a constant to each value does not affect the standard deviation, while multiplying by 3 scales the standard deviation by 3.\nTherefore, the new standard deviation is 3p. [Option (B)]"
      },
      {
        "id": "m_c8_q8",
        "chapterNumber": 8,
        "chapterName": "Statistics and Probability",
        "questionNumber": 8,
        "question": "If the mean and coefficient of variation of a data are 4 and 87.5% respectively, then the standard deviation is",
        "options": [
          {"id": "A", "text": "3.5"},
          {"id": "B", "text": "3"},
          {"id": "C", "text": "4.5"},
          {"id": "D", "text": "2.5"}
        ],
        "correctAnswer": "A",
        "explanation": "CV = (σ / x̄) × 100% ⇒ 87.5 = (σ / 4) × 100 ⇒ σ = (87.5 × 4) / 100 = 350 / 100 = 3.5. [Option (A)]"
      },
      {
        "id": "m_c8_q9",
        "chapterNumber": 8,
        "chapterName": "Statistics and Probability",
        "questionNumber": 9,
        "question": "Which of the following is incorrect?",
        "options": [
          {"id": "A", "text": "P(A) > 1"},
          {"id": "B", "text": "0 ≤ P(A) ≤ 1"},
          {"id": "C", "text": "P(∅) = 0"},
          {"id": "D", "text": "P(A) + P(A') = 1"}
        ],
        "correctAnswer": "A",
        "explanation": "Probability of any event is always bounded between 0 and 1 (0 ≤ P(A) ≤ 1). Hence P(A) > 1 is impossible and incorrect. [Option (A)]"
      },
      {
        "id": "m_c8_q10",
        "chapterNumber": 8,
        "chapterName": "Statistics and Probability",
        "questionNumber": 10,
        "question": "The probability of selecting a red marble at random from a jar containing p red, q blue and r green marbles is",
        "options": [
          {"id": "A", "text": "q / (p + q + r)"},
          {"id": "B", "text": "p / (p + q + r)"},
          {"id": "C", "text": "(p + q) / (p + q + r)"},
          {"id": "D", "text": "(p + r) / (p + q + r)"}
        ],
        "correctAnswer": "B",
        "explanation": "Number of red marbles = p.\nTotal number of marbles in jar = p + q + r.\nP(red marble) = p / (p + q + r). [Option (B)]"
      },
      {
        "id": "m_c8_q11",
        "chapterNumber": 8,
        "chapterName": "Statistics and Probability",
        "questionNumber": 11,
        "question": "A page is selected at random from a book. The probability that the digit at the units place of the page number chosen is less than 7 is",
        "options": [
          {"id": "A", "text": "3/10"},
          {"id": "B", "text": "7/9"},
          {"id": "C", "text": "7/10"},
          {"id": "D", "text": "3/7"}
        ],
        "correctAnswer": "C",
        "explanation": "Possible digits at units place S = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} ⇒ n(S) = 10.\nDigits less than 7: A = {0, 1, 2, 3, 4, 5, 6} ⇒ n(A) = 7.\nP(A) = n(A) / n(S) = 7/10. [Option (C)]"
      },
      {
        "id": "m_c8_q12",
        "chapterNumber": 8,
        "chapterName": "Statistics and Probability",
        "questionNumber": 12,
        "question": "The probability of getting a job for a person is x/3. If the probability of not getting the job is 2/3, then the value of x is",
        "options": [
          {"id": "A", "text": "2"},
          {"id": "B", "text": "1"},
          {"id": "C", "text": "3"},
          {"id": "D", "text": "1.5"}
        ],
        "correctAnswer": "B",
        "explanation": "P(E) + P(not E) = 1 ⇒ x/3 + 2/3 = 1 ⇒ (x + 2)/3 = 1 ⇒ x + 2 = 3 ⇒ x = 1. [Option (B)]"
      },
      {
        "id": "m_c8_q13",
        "chapterNumber": 8,
        "chapterName": "Statistics and Probability",
        "questionNumber": 13,
        "question": "In a lucky draw contest, 135 tickets were sold. If the probability of winning is 1/9, then the number of tickets bought is",
        "options": [
          {"id": "A", "text": "5"},
          {"id": "B", "text": "10"},
          {"id": "C", "text": "15"},
          {"id": "D", "text": "20"}
        ],
        "correctAnswer": "C",
        "explanation": "Let number of tickets bought be x. Total tickets n(S) = 135.\nP(winning) = x / 135 = 1/9 ⇒ x = 135 / 9 = 15 tickets. [Option (C)]"
      },
      {
        "id": "m_c8_q14",
        "chapterNumber": 8,
        "chapterName": "Statistics and Probability",
        "questionNumber": 14,
        "question": "If a letter is chosen at random from the English alphabets {a, b, ..., z}, then the probability that the letter chosen precedes 'x' is",
        "options": [
          {"id": "A", "text": "12/13"},
          {"id": "B", "text": "1/13"},
          {"id": "C", "text": "23/26"},
          {"id": "D", "text": "3/26"}
        ],
        "correctAnswer": "C",
        "explanation": "Total letters n(S) = 26.\nLetters preceding 'x' are a through w, which is 23 letters (24th is x).\nProbability = 23 / 26. [Option (C)]"
      },
      {
        "id": "m_c8_q15",
        "chapterNumber": 8,
        "chapterName": "Statistics and Probability",
        "questionNumber": 15,
        "question": "A purse contains 10 notes of ₹2000, 15 notes of ₹500, and 25 notes of ₹200. One note is drawn at random. What is the probability that the note is either a ₹500 or ₹200 note?",
        "options": [
          {"id": "A", "text": "1/5"},
          {"id": "B", "text": "3/10"},
          {"id": "C", "text": "2/3"},
          {"id": "D", "text": "4/5"}
        ],
        "correctAnswer": "D",
        "explanation": "Total notes = 10 + 15 + 25 = 50 notes.\nFavorable notes (₹500 or ₹200) = 15 + 25 = 40 notes.\nProbability = 40 / 50 = 4/5. [Option (D)]"
      }
    ]
  }
]

# Apply vertical fractions for math division
MAPPING = {
    '(16/5) |(x z²) / y|': '<span class="math-fraction"><span class="math-numerator">16</span><span class="math-denominator">5</span></span> |<span class="math-fraction"><span class="math-numerator">x z²</span><span class="math-denominator">y</span></span>|',
    '(16/5) |(x² z⁴) / y²|': '<span class="math-fraction"><span class="math-numerator">16</span><span class="math-denominator">5</span></span> |<span class="math-fraction"><span class="math-numerator">x² z⁴</span><span class="math-denominator">y²</span></span>|',
    '(16/5) |(y) / (x z²)|': '<span class="math-fraction"><span class="math-numerator">16</span><span class="math-denominator">5</span></span> |<span class="math-fraction"><span class="math-numerator">y</span><span class="math-denominator">x z²</span></span>|',
    '(16/5) |(y²) / (x² z⁴)|': '<span class="math-fraction"><span class="math-numerator">16</span><span class="math-denominator">5</span></span> |<span class="math-fraction"><span class="math-numerator">y²</span><span class="math-denominator">x² z⁴</span></span>|',
    '(p + q) / (p + q + r)': '<span class="math-fraction"><span class="math-numerator">p + q</span><span class="math-denominator">p + q + r</span></span>',
    '(p + r) / (p + q + r)': '<span class="math-fraction"><span class="math-numerator">p + r</span><span class="math-denominator">p + q + r</span></span>',
    '(x² + 10) / [(x² - 25)(x + 1)]': '<span class="math-fraction"><span class="math-numerator">x² + 10</span><span class="math-denominator">(x² - 25)(x + 1)</span></span>',
    '(x² + 7x + 40) / [(x - 5)(x + 5)]': '<span class="math-fraction"><span class="math-numerator">x² + 7x + 40</span><span class="math-denominator">(x - 5)(x + 5)</span></span>',
    '(x² - 7x + 40) / (x - 5)': '<span class="math-fraction"><span class="math-numerator">x² - 7x + 40</span><span class="math-denominator">x - 5</span></span>',
    '(x² - 7x + 40) / [(x² - 25)(x + 1)]': '<span class="math-fraction"><span class="math-numerator">x² - 7x + 40</span><span class="math-denominator">(x² - 25)(x + 1)</span></span>',
    '(y⁴ + 1) / y²': '<span class="math-fraction"><span class="math-numerator">y⁴ + 1</span><span class="math-denominator">y²</span></span>',
    '-2/3': '-<span class="math-fraction"><span class="math-numerator">2</span><span class="math-denominator">3</span></span>',
    '-3/2': '-<span class="math-fraction"><span class="math-numerator">3</span><span class="math-denominator">2</span></span>',
    '1 / (6x²)': '<span class="math-fraction"><span class="math-numerator">1</span><span class="math-denominator">6x²</span></span>',
    '1/13': '<span class="math-fraction"><span class="math-numerator">1</span><span class="math-denominator">13</span></span>',
    '1/24': '<span class="math-fraction"><span class="math-numerator">1</span><span class="math-denominator">24</span></span>',
    '1/25': '<span class="math-fraction"><span class="math-numerator">1</span><span class="math-denominator">25</span></span>',
    '1/27': '<span class="math-fraction"><span class="math-numerator">1</span><span class="math-denominator">27</span></span>',
    '1/3': '<span class="math-fraction"><span class="math-numerator">1</span><span class="math-denominator">3</span></span>',
    '1/5': '<span class="math-fraction"><span class="math-numerator">1</span><span class="math-denominator">5</span></span>',
    '1/81': '<span class="math-fraction"><span class="math-numerator">1</span><span class="math-denominator">81</span></span>',
    '1/√3': '<span class="math-fraction"><span class="math-numerator">1</span><span class="math-denominator">√3</span></span>',
    '10/3 cm': '<span class="math-fraction"><span class="math-numerator">10</span><span class="math-denominator">3</span></span> cm',
    '10/3 π': '<span class="math-fraction"><span class="math-numerator">10</span><span class="math-denominator">3</span></span> π',
    '12/13': '<span class="math-fraction"><span class="math-numerator">12</span><span class="math-denominator">13</span></span>',
    '2 / (3x²)': '<span class="math-fraction"><span class="math-numerator">2</span><span class="math-denominator">3x²</span></span>',
    '2 / (9x²)': '<span class="math-fraction"><span class="math-numerator">2</span><span class="math-denominator">9x²</span></span>',
    '2/3': '<span class="math-fraction"><span class="math-numerator">2</span><span class="math-denominator">3</span></span>',
    '20/3 π': '<span class="math-fraction"><span class="math-numerator">20</span><span class="math-denominator">3</span></span> π',
    '21(y² - 2y + 1) / (3y³)': '<span class="math-fraction"><span class="math-numerator">21(y² - 2y + 1)</span><span class="math-denominator">3y³</span></span>',
    '23/26': '<span class="math-fraction"><span class="math-numerator">23</span><span class="math-denominator">26</span></span>',
    '3 / (2x²)': '<span class="math-fraction"><span class="math-numerator">3</span><span class="math-denominator">2x²</span></span>',
    '3/10': '<span class="math-fraction"><span class="math-numerator">3</span><span class="math-denominator">10</span></span>',
    '3/2': '<span class="math-fraction"><span class="math-numerator">3</span><span class="math-denominator">2</span></span>',
    '3/26': '<span class="math-fraction"><span class="math-numerator">3</span><span class="math-denominator">26</span></span>',
    '3/7': '<span class="math-fraction"><span class="math-numerator">3</span><span class="math-denominator">7</span></span>',
    '31/2 m': '<span class="math-fraction"><span class="math-numerator">31</span><span class="math-denominator">2</span></span> m',
    '4/3 π': '<span class="math-fraction"><span class="math-numerator">4</span><span class="math-denominator">3</span></span> π',
    '4/5': '<span class="math-fraction"><span class="math-numerator">4</span><span class="math-denominator">5</span></span>',
    '56/9 πh² sq. units': '<span class="math-fraction"><span class="math-numerator">56</span><span class="math-denominator">9</span></span> πh² sq. units',
    '7 / (9y)': '<span class="math-fraction"><span class="math-numerator">7</span><span class="math-denominator">9y</span></span>',
    '7/10': '<span class="math-fraction"><span class="math-numerator">7</span><span class="math-denominator">10</span></span>',
    '7/9': '<span class="math-fraction"><span class="math-numerator">7</span><span class="math-denominator">9</span></span>',
    '8/9 πh² sq. units': '<span class="math-fraction"><span class="math-numerator">8</span><span class="math-denominator">9</span></span> πh² sq. units',
    '9/8 πh² sq. units': '<span class="math-fraction"><span class="math-numerator">9</span><span class="math-denominator">8</span></span> πh² sq. units',
    '9y / 7': '<span class="math-fraction"><span class="math-numerator">9y</span><span class="math-denominator">7</span></span>',
    '9y³ / (21y - 21)': '<span class="math-fraction"><span class="math-numerator">9y³</span><span class="math-denominator">21y - 21</span></span>',
    'If 5x = sec θ and 5/x = tan θ, then x² - 1/x² is equal to': 'If 5x = sec θ and <span class="math-fraction"><span class="math-numerator">5</span><span class="math-denominator">x</span></span> = tan θ, then x² - <span class="math-fraction"><span class="math-numerator">1</span><span class="math-denominator">x²</span></span> is equal to',
    'If f(x) = 2x² and g(x) = 1/(3x), then f ∘ g is': 'If f(x) = 2x² and g(x) = <span class="math-fraction"><span class="math-numerator">1</span><span class="math-denominator">3x</span></span>, then f ∘ g is',
    'If the slope of a line is -1/√3, then the slope of the perpendicular bisector of the line is': 'If the slope of a line is -<span class="math-fraction"><span class="math-numerator">1</span><span class="math-denominator">√3</span></span>, then the slope of the perpendicular bisector of the line is',
    "If the slope of the line joining (12, 3) and (4, a) is 1/8, then the value of 'a' is": "If the slope of the line joining (12, 3) and (4, a) is <span class=\"math-fraction\"><span class=\"math-numerator\">1</span><span class=\"math-denominator\">8</span></span>, then the value of 'a' is",
    'If triangles ABC and EDF are similar such that AB/ED = BC/DF, then': 'If triangles ABC and EDF are similar such that <span class=\"math-fraction\"><span class=\"math-numerator\">AB</span><span class=\"math-denominator\">ED</span></span> = <span class=\"math-fraction\"><span class=\"math-numerator\">BC</span><span class=\"math-denominator\">DF</span></span>, then',
    'In a lucky draw contest, 135 tickets were sold. If the probability of winning is 1/9, then the number of tickets bought is': 'In a lucky draw contest, 135 tickets were sold. If the probability of winning is <span class=\"math-fraction\"><span class=\"math-numerator\">1</span><span class=\"math-denominator\">9</span></span>, then the number of tickets bought is',
    'The next term of the sequence 3/16, 1/8, 1/12, 1/18, ... is': 'The next term of the sequence <span class=\"math-fraction\"><span class=\"math-numerator\">3</span><span class=\"math-denominator\">16</span></span>, <span class=\"math-fraction\"><span class=\"math-numerator\">1</span><span class=\"math-denominator\">8</span></span>, <span class=\"math-fraction\"><span class=\"math-numerator\">1</span><span class=\"math-denominator\">12</span></span>, <span class=\"math-fraction\"><span class=\"math-numerator\">1</span><span class=\"math-denominator\">18</span></span>, ... is',
    'The probability of getting a job for a person is x/3. If the probability of not getting the job is 2/3, then the value of x is': 'The probability of getting a job for a person is <span class=\"math-fraction\"><span class=\"math-numerator\">x</span><span class=\"math-denominator\">3</span></span>. If the probability of not getting the job is <span class=\"math-fraction\"><span class=\"math-numerator\">2</span><span class=\"math-denominator\">3</span></span>, then the value of x is',
    'The quotient of (3y - 3)/y divided by (7y - 7)/(3y²) is': 'The quotient of <span class=\"math-fraction\"><span class=\"math-numerator\">3y - 3</span><span class=\"math-denominator\">y</span></span> divided by <span class=\"math-fraction\"><span class=\"math-numerator\">7y - 7</span><span class=\"math-denominator\">3y²</span></span> is',
    'The square root of (256 x⁸ y⁴ z¹⁰) / (25 x⁶ y⁶ z⁶) is equal to': 'The square root of <span class=\"math-fraction\"><span class=\"math-numerator\">256 x⁸ y⁴ z¹⁰</span><span class=\"math-denominator\">25 x⁶ y⁶ z⁶</span></span> is equal to',
    'The total surface area of a cylinder whose radius is 1/3 of its height h is': 'The total surface area of a cylinder whose radius is <span class=\"math-fraction\"><span class=\"math-numerator\">1</span><span class=\"math-denominator\">3</span></span> of its height h is',
    '[ (y + 1)/y ]²': '[ <span class=\"math-fraction\"><span class=\"math-numerator\">y + 1</span><span class=\"math-denominator\">y</span></span> ]²',
    '[ y + (1/y) ]² - 2': '[ y + <span class=\"math-fraction\"><span class=\"math-numerator\">1</span><span class=\"math-denominator\">y</span></span> ]² - 2',
    '[ y - (1/y) ]² + 2': '[ y - <span class=\"math-fraction\"><span class=\"math-numerator\">1</span><span class=\"math-denominator\">y</span></span> ]² + 2',
    'b / 2': '<span class=\"math-fraction\"><span class=\"math-numerator\">b</span><span class=\"math-denominator\">2</span></span>',
    'b / 3': '<span class=\"math-fraction\"><span class=\"math-numerator\">b</span><span class=\"math-denominator\">3</span></span>',
    'b / √3': '<span class=\"math-fraction\"><span class=\"math-numerator\">b</span><span class=\"math-denominator\">√3</span></span>',
    'h(1 + tan θ) / (1 - tan θ)': '<span class=\"math-fraction\"><span class=\"math-numerator\">h(1 + tan θ)</span><span class=\"math-denominator\">1 - tan θ</span></span>',
    'h(1 - tan θ) / (1 + tan θ)': '<span class=\"math-fraction\"><span class=\"math-numerator\">h(1 - tan θ)</span><span class=\"math-denominator\">1 + tan θ</span></span>',
    'p / (p + q + r)': '<span class=\"math-fraction\"><span class=\"math-numerator\">p</span><span class=\"math-denominator\">p + q + r</span></span>',
    'q / (p + q + r)': '<span class=\"math-fraction\"><span class=\"math-numerator\">q</span><span class=\"math-denominator\">p + q + r</span></span>',
    'sin² θ + 1 / (1 + tan² θ) is equal to': 'sin² θ + <span class=\"math-fraction\"><span class=\"math-numerator\">1</span><span class=\"math-denominator\">1 + tan² θ</span></span> is equal to',
    'x / (2√2)': '<span class=\"math-fraction\"><span class=\"math-numerator\">x</span><span class=\"math-denominator\">2√2</span></span>',
    'x / √2': '<span class=\"math-fraction\"><span class=\"math-numerator\">x</span><span class=\"math-denominator\">√2</span></span>',
    'x/(x² - 25) - 8/(x² + 6x + 5) is equal to': '<span class=\"math-fraction\"><span class=\"math-numerator\">x</span><span class=\"math-denominator\">x² - 25</span></span> - <span class=\"math-fraction\"><span class=\"math-numerator\">8</span><span class=\"math-denominator\">x² + 6x + 5</span></span> is equal to',
    'x²/a² + y²/b² = 1': '<span class=\"math-fraction\"><span class=\"math-numerator\">x²</span><span class=\"math-denominator\">a²</span></span> + <span class=\"math-fraction\"><span class=\"math-numerator\">y²</span><span class=\"math-denominator\">b²</span></span> = 1',
    'x²/a² - y²/b² = 1': '<span class=\"math-fraction\"><span class=\"math-numerator\">x²</span><span class=\"math-denominator\">a²</span></span> - <span class=\"math-fraction\"><span class=\"math-numerator\">y²</span><span class=\"math-denominator\">b²</span></span> = 1',
    'y² + 1/y² is not equal to': 'y² + <span class=\"math-fraction\"><span class=\"math-numerator\">1</span><span class=\"math-denominator\">y²</span></span> is not equal to',
    'y²/a² - x²/b² = 1': '<span class=\"math-fraction\"><span class=\"math-numerator\">y²</span><span class=\"math-denominator\">a²</span></span> - <span class=\"math-fraction\"><span class=\"math-numerator\">x²</span><span class=\"math-denominator\">b²</span></span> = 1',
    'y²/b² - x²/a² = 1': '<span class=\"math-fraction\"><span class=\"math-numerator\">y²</span><span class=\"math-denominator\">b²</span></span> - <span class=\"math-fraction\"><span class=\"math-numerator\">x²</span><span class=\"math-denominator\">a²</span></span> = 1'
}

import re

def format_roots(text):
    if not isinstance(text, str):
        return text
    text = re.sub(
        r'√\(([^)]+)\)',
        r'<span class="math-sqrt"><svg class="sqrt-surd" viewBox="0 0 12 24" preserveAspectRatio="none"><path d="M1 14.5 L3.5 13 L6.5 22.5 L12 1.5" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="miter"/></svg><span class="sqrt-radicand">\\1</span></span>',
        text
    )
    text = re.sub(
        r'√([0-9a-zA-Z²³⁴⁵⁶⁷⁸⁹¹⁰θπ]+)',
        r'<span class="math-sqrt"><svg class="sqrt-surd" viewBox="0 0 12 24" preserveAspectRatio="none"><path d="M1 14.5 L3.5 13 L6.5 22.5 L12 1.5" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="miter"/></svg><span class="sqrt-radicand">\\1</span></span>',
        text
    )
    return text

for ch in chapters:
    for q in ch['questions']:
        if q['question'] in MAPPING:
            q['question'] = MAPPING[q['question']]
        q['question'] = format_roots(q['question'])
        for opt in q['options']:
            if opt['text'] in MAPPING:
                opt['text'] = MAPPING[opt['text']]
            opt['text'] = format_roots(opt['text'])

# Write to JSON
with open('data/maths_data.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, indent=2, ensure_ascii=False)

# Write to JS
with open('data/maths_data.js', 'w', encoding='utf-8') as f:
    f.write('// Class 10 Tamil Nadu Mathematics MCQ Dataset\n')
    f.write('window.MATHS_CHAPTERS = ' + json.dumps(chapters, indent=2, ensure_ascii=False) + ';\n')

total_q = sum(len(c['questions']) for c in chapters)
print(f"Generated {len(chapters)} chapters with a total of {total_q} questions!")
