# Data Bench
One Standard Repo to unify your data projects on GitHub

# Data Science Project Planning
- I chose Critical Chain for its ease of use
  - Supplemental Reading: https://www.simplilearn.com/what-is-critical-chain-project-management-rar68-article
  - Good Explanation: https://www.knowledgehut.com/tutorials/project-management/critical-chain-method
- `README.md` markdown documents can be your friend as they are multifaceted tools
  - Markdown code allows me to take this
```
    gantt
    title A Gantt Diagram
    dateFormat  YYYY-MM-DD
    section Initial Phase
    Topic Selection                     :a1, 2021-09-19, 7d
    Suitabile/Practical                 :after a1  , 7d
    section Implement
    Topic Formulation                   :b1, 2021-09-26, 7d
    Debugging/Cleaning                  :after b1  , 7d
    section Test/Debug01
    Scope Document                      :c1, 2021-10-03, 7d
    Suitable vs Practical               :after c1  , 7d
    section Test/Debug02
    API access changes                  :c2, 2021-10-10, 7d
    API data triage                     :after c1  , 14d
    section Implement
    Upskill Team Members on GitHub      :e1, 2021-10-17, 28d
    Define and adapt critical path                :after a1  , 49d
    section Implement
    BiWeek Scrum Review               :f1, 2021-10-17, 35d
    Trial Run 1                        :after e1  , 7d
    section Implement
    Functional Triage 1               :f2, 2021-11-14, 7d
    Presentation Dry Run                :after e1  , 14d
    Trial Run 2                        :after f2  , 7d
    section Draft Doc
    Finalize Design, Data, Functions and write tests          :f1, 2021-10-24, 42d
    Trial Run 3                        :after g1  , 7d
    section Revised Doc
    Functional Triage 2               :g1, 2021-11-21, 7d
    section Revised Doc 2
    Functional Triage 3               :h1, 2021-11-28, 7d
    section Final Doc
    Trial Run 4                       :after h1  , 7d
    Functional Triage 4               :i1, 2021-12-05, 7d
    Record & Revise                   :after i1  , 7d
    Final Run 3                       :after i1  , 7d

``` 

- Now load Mermaid, click here for a tutorial http://mermaid-js.github.io/mermaid/#/n00b-gettingStarted
- I'm partial to Mermaid see below for the Gantt chart was created from the code above

[![](https://mermaid.ink/img/pako:eNqNlclu2zAQhl9loENPdizSjhfd0qpJczBgJC6KAr5Q1EgiIlECSSVIA797qaWSY1t2CR_kIefnNwsxHw7PQ3Q8J2bSmJ0Eu4wwKcIdPFQm8AWLFcuarZAZvM9VxgzAb7vG6_XY95s9jdyIXMKjFEawFDYJ09hsbfNCcHjGtD1ybnmMjIC6lIzd1ZisRrAIG-fnUhgWiBQnG8WsP7fap86RQQWMAPSOHVBWpJihNIcwVRRlygZwvOAAhs57TR-DMo6FjCffUmTSfsAQTHAWZovaTGoVl7Tx8bxA8HNeVoxwPjn8Hw9xx-70ODm2XK8ahtLT8vBrPLTZuds8AuMctQaeMBmjPsdDex7i9rKVs20SBkbZvsGBSh_wkNnlav0s9ItIU8vJMlhjFqDSYI89CPOjDFpBPMgOWdjvZVeuSEgEJkNgISsMcCWaFBXMJBe7aLa6DPZV_EJ8sdVTZQZP-Crw7VguOsKa3raSW1U9kKdSAoGB1bLg_3T0fSlru9XcNmknJyhdvexv1ituFGqr07wDX73XUJdQunr1MdArMUT0XAy-srtV27cxCIsv_tiHgFrEcgS-7aJRF5qua_hmq4dgbMvqgTRTG9uMniBOryDGZ9NcVVVjeAB5kujj2L2Y9Imm5KIm0CHVY1wvOVRdnqrW2es5-8Bnl-NOPsV9CnLs7okOhI7d2971CXmuQvjSxjd8o_h8Y819qUJn3ZyRk6GdQiK0k-ujsu0ck9gXsXM8-xlixMrU7Jyd3NujrDT587vkjmdUiSOnLKox1s41x4tYqjvr91CYXHXGNGch2r8fjnkv6jEptLGSPJeRiCt7qVJrTowptDeZVNs3sTBJGdzwPJtoESZMmeR1NZ_M6XzJ6BTniym7nU5DHpDVMqIzEoULl1Dm7PcjB-v7181Mrkfz_i8yxwvO?type=png)](https://mermaid.live/edit#pako:eNqNlclu2zAQhl9loENPdizSjhfd0qpJczBgJC6KAr5Q1EgiIlECSSVIA797qaWSY1t2CR_kIefnNwsxHw7PQ3Q8J2bSmJ0Eu4wwKcIdPFQm8AWLFcuarZAZvM9VxgzAb7vG6_XY95s9jdyIXMKjFEawFDYJ09hsbfNCcHjGtD1ybnmMjIC6lIzd1ZisRrAIG-fnUhgWiBQnG8WsP7fap86RQQWMAPSOHVBWpJihNIcwVRRlygZwvOAAhs57TR-DMo6FjCffUmTSfsAQTHAWZovaTGoVl7Tx8bxA8HNeVoxwPjn8Hw9xx-70ODm2XK8ahtLT8vBrPLTZuds8AuMctQaeMBmjPsdDex7i9rKVs20SBkbZvsGBSh_wkNnlav0s9ItIU8vJMlhjFqDSYI89CPOjDFpBPMgOWdjvZVeuSEgEJkNgISsMcCWaFBXMJBe7aLa6DPZV_EJ8sdVTZQZP-Crw7VguOsKa3raSW1U9kKdSAoGB1bLg_3T0fSlru9XcNmknJyhdvexv1ituFGqr07wDX73XUJdQunr1MdArMUT0XAy-srtV27cxCIsv_tiHgFrEcgS-7aJRF5qua_hmq4dgbMvqgTRTG9uMniBOryDGZ9NcVVVjeAB5kujj2L2Y9Imm5KIm0CHVY1wvOVRdnqrW2es5-8Bnl-NOPsV9CnLs7okOhI7d2971CXmuQvjSxjd8o_h8Y819qUJn3ZyRk6GdQiK0k-ujsu0ck9gXsXM8-xlixMrU7Jyd3NujrDT587vkjmdUiSOnLKox1s41x4tYqjvr91CYXHXGNGch2r8fjnkv6jEptLGSPJeRiCt7qVJrTowptDeZVNs3sTBJGdzwPJtoESZMmeR1NZ_M6XzJ6BTniym7nU5DHpDVMqIzEoULl1Dm7PcjB-v7181Mrkfz_i8yxwvO)

- While this is not perfect its a great way to align Critical Chain Project Management to Data Science projects
- Mermaid can do many things
- Future Feature is to have Mermaid pull flowchart function from my python code.


# Errata
- Any sufficently useful code will create errors
- Creating a bug database


# Requirements
- Python 3.7


# Installation
- git clone `repo name` and press enter in your terminal of choice

# Features


# Future Features


# LICENSE

The [Commons Clause](https://commonsclause.com) is a License Condition drafted by Heather Meeker and contributed by [FOSSA](https://fossa.io).

```plaintext
“Commons Clause” License Condition v1.0

The Software is provided to you by the Licensor under the License, as defined below, subject to the following condition.

Without limiting other conditions in the License, the grant of rights under the License will not include, and the License does not grant to you,  right to Sell the Software.

For purposes of the foregoing, “Sell” means practicing any or all of the rights granted to you under the License to provide to third parties, for a fee or other consideration (including without limitation fees for hosting or consulting/ support services related to the Software), a product or service whose value derives, entirely or substantially, from the functionality of the Software.  Any license notice or attribution required by the License must also include this Commons Cause License Condition notice.

Software: [Data_Bench]
License: [i.e. Apache 2.0]
Licensor: [Data Talking]
```

## About

Read about the Commons Clause and its purpose on the public [FAQ](https://commonsclause.com/#faq)

## License

This repository is under the [Public Domain](https://creativecommons.org/publicdomain/zero/1.0/legalcode).