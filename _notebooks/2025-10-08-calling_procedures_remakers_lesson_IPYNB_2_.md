---
layout: post
courses: {'csp': {'week': 1}}
categories: ['Python', 'Calling-Procedures']
lesson_language: Python
lesson_topic: Calling-Procedures
lesson_part: interactive
lesson_type: lesson
toc: True
codemirror: True
challenge_submit: True
assignment: True
comments: False
title: 3.12 Calling Procedures
description: 3.12 Calling Procedures
permalink: /csp/big-idea-3/calling-procedures/p4/lesson
author: Samanvi Yachareni, Joan Kim, Ainsley Albert
date: 2026-09-16
---

### 3.12 Calling Procedures

Every time you send a text message, your phone encodes the characters, transmits a wireless signal to a cell tower, and routes it to your friend. You don’t route network packets by hand — you just press send. That’s calling a procedure: the steps are saved, and you run them whenever you need them.

#### What is calling a procedure?
A procedure (a function in Python) is a named set of re-usable code instructions.

- You can call a procedure multiple times with different input values without having to rewrite it
- Different from defining the procedure: defining is creating it, calling is using it
- Calling allows you to run the same set of instructions whenever you need them without rewriting the lines of code.
#### Passing Inputs (Parameters)
You can make procedures more flexible by giving them parameters—input variables that hold data passed into the procedure when you call it.

- Parameters act as temporary placeholders inside the procedure definition.
- Arguments are the actual values you send into the procedure when you call it.
This allows a single procedure to run the same set of instructions on completely different data without rewriting the code.

Python Example:

- Use def to define the function/procedure
- To call a procedure write the name of the procedure followed by parenthesis, and variables if included

```
# 1. DEFINE the procedure with a parameter (variable input)
def send_notification(username):
    print("New message for " + username + "!")

# 2. CALL the procedure passing different inputs
send_notification("Joan")
```

#### Calling Procedures Inside Procedures (Decomposition)
In computer science, large problems are broken down into smaller steps—a process called decomposition. You can call a helper procedure inside an outer procedure to handle a specific part of a task. Each step can become its own procedure, and one procedure can call another one. This allows programs to become easier to read, use, and debug.

Python Example:

```
# Helper procedure: Calculates the final price with sales tax
def calculate_tax(price):
    return price * 1.07

# Outer procedure: Handles the checkout process
def checkout(item_name, base_price):
    total = calculate_tax(base_price)  # Calling the helper procedure
    print("Purchased " + item_name + " for $" + str(total))

# Execution starts here
checkout("Sneakers", 80.0)
```

#### Key Takeaways

- Defining vs. Calling: Defining a procedure (def) creates the instructions; calling a procedure using its name with parentheses () actually executes them.
- Reusability: Calling procedures allows you to run the same code multiple times throughout your program without retyping it.
- Decomposition: Breaking complex tasks into smaller, manageable steps makes code easier to read, debug, and maintain.
- Helper Procedures: Outer procedures can call smaller helper procedures to handle specific sub-tasks and combine the results.
#### 1. LxD Cycle Process
**Empathize:** I noticed students were copy-pasting repetitive blocks of code throughout their Python scripts rather than writing modular functions. This made their code cluttered, difficult to debug, and hard to update.

**Define:**

- POV: AP CSP students need a clear way to practice writing and calling Python procedures so they can eliminate code duplication and organize programs logically.
- Learning Goal: Students will define procedures with parameters and call helper procedures within outer functions using Python.
**Ideate:**

- HMW Question: How might we teach procedural decomposition and calling syntax in under 2 minutes so students can quickly jump to hands-on execution?
- Activity: A quick code-refactoring challenge where students convert duplicate print/math statements into a modular function with helper procedures.
**Prototype & Test:** During peer feedback, my team mentioned that the original reading material was too long and wordy. I streamlined the explanation down to core bullet points and replaced the open-ended coding task with two runnable code challenges.

#### 2. Lesson Plan

- **Learning Objective:** Define a Python procedure with parameters, call it using arguments, and utilize helper procedures to decompose tasks.
- **Success Criteria:** You can identify the difference between defining and calling a function, pass parameters correctly, and execute a helper procedure inside an outer procedure in the code runner.
#### 3. Hacks & Practice Tasks

#### Popcorn Hack (In-Class Code Runner)
Task: The code below prints receipt lines manually. Refactor it by defining a procedure apply_discount(price) that takes a price, subtracts $5, and returns the new price. Then call it inside print_receipt.

{% capture popcorn_challenge %}
Refactor the receipt code by defining an `apply_discount(price)` helper procedure and calling it inside `print_receipt`.
{% endcapture %}

{% capture popcorn_code %}
# TODO: Define the apply_discount(price) helper procedure here

def print_receipt(item, original_price):
    # TODO: Call apply_discount here to get the final_price
    final_price = original_price
    print("Item: " + item + " | Final Price: $" + str(final_price))

# Test your code
print_receipt("Game Controller", 60.0)
{% endcapture %}

{% include runners/code.html runner_id="procedures-popcorn" language="python" challenge=popcorn_challenge code=popcorn_code %}

#### Homework Hack (Code Runner Challenge)
Task: Refactor the messy code below.

- Create a helper procedure is_passing(score) that returns True if score >= 70, and False otherwise.
- Create an outer procedure evaluate_student(name, score) that calls is_passing(score).
- If passing, print "| Status: Passed". Otherwise, print "| Status: Needs Review".
- Call evaluate_student twice with different values.

{% capture homework_challenge %}
Create a helper procedure `is_passing(score)` and an outer procedure `evaluate_student(name, score)` that calls it twice with different values.
{% endcapture %}

{% capture homework_code %}
# TODO: Write your helper procedure 'is_passing' here

# TODO: Write your outer procedure 'evaluate_student' here

# TODO: Call evaluate_student twice below
{% endcapture %}

{% include runners/code.html runner_id="procedures-homework" language="python" challenge=homework_challenge code=homework_code %}

#### 4. Grading Plan (1 Point Total)
Classroom Rubric

- 0.2 points: Popcorn Completion: Student successfully defined apply_discount, integrated it into print_receipt, and ran the cell cleanly using %%python.
- 0.8 points: Homework Completion
- 0.3 Parameter & Procedure Definition: Correctly uses def with appropriate parameters for both procedures.
- 0.3 Helper Calling Logic: Calls is_passing inside evaluate_student to handle the conditional check.
- 0.2 Execution & Outputs: Calls the outer procedure twice with different inputs and produces correct status outputs.
#### Quick Validation Checklist
- [ ] Present: `%%python` and `UI_RUNNER` headers in code blocks.
- [ ] Present: Helper procedure called inside the main procedure.
- [ ] Absent: Hardcoded repetitive logic or global variables outside of procedures.

#### 5. Lesson Revisions & Feedback Evidence
**Feedback Received:** Peer reviewers noted that the original lesson was dense, taking over 5 minutes to read, and lacked interactive execution elements on the page.

**Revision Made:** Reduced explanation text to three bullet points, replaced theoretical game discussions with direct in-browser Code Runner challenges, and structured the Popcorn Hack so it can be completed in under 2 minutes.

By Joan Kim, Samanvi Yachareni, Ainsley Albert

<style>
  .assignment-submission {
    margin-top: 28px !important;
    padding: 28px 20px 20px !important;
    background: #0a0d11 !important;
    border: 2px solid #18a7e0 !important;
    border-radius: 22px !important;
    color: #f3f4f6 !important;
  }

  .assignment-submission h3 {
    color: #f3f4f6 !important;
    font-size: clamp(2rem, 2vw, 2.7rem) !important;
    margin-bottom: 26px !important;
  }

  .assignment-submission-icon {
    color: #27b9ec !important;
  }

  .submission-options {
    gap: 18px !important;
    margin-bottom: 20px !important;
  }

  .submission-tab {
    min-width: 220px;
    padding: 14px 22px !important;
    background: rgba(16, 20, 32, 0.9) !important;
    border: 2px solid #1fb3ea !important;
    border-radius: 14px !important;
    color: #f3f4f6 !important;
    font-size: 1.05rem !important;
    font-weight: 600 !important;
  }

  .submission-tab:hover,
  .submission-tab.active {
    background: #101420 !important;
    border-color: #4dc9f4 !important;
    color: #ffffff !important;
  }

  .assignment-submission .form-group label {
    color: #f3f4f6 !important;
  }

  .assignment-submission .form-group input,
  .assignment-submission .form-group textarea,
  .assignment-submission .file-upload-area {
    background: #101420 !important;
    border-color: #31536a !important;
    color: #f3f4f6 !important;
  }

  @media (max-width: 700px) {
    .assignment-submission {
      padding: 22px 14px 16px !important;
    }

    .submission-tab {
      width: 100%;
      min-width: 0;
    }
  }
</style>
