# 🧩 Static Variable & Static Method in Python (Sample Class)

## 📌 Description

This Python program demonstrates the concept of a **static (class) variable** and a **static method**. It shows how a single shared variable (`z`) is common across all objects of a class.

---

## 🚀 Features

* Uses a **class variable** (`z`) shared by all objects
* Uses **instance variables** (`x`, `y`) unique to each object
* Updates shared data using objects
* Implements a **static method**

---

## 🛠️ How It Works

1. A class `Sample` is created with:

   * `z` → static (class) variable
   * `x`, `y` → instance variables

2. Method `setData(x, y, z)`:

   * Assigns values to `x` and `y` (object-specific)
   * Updates `Sample.z` (shared across all objects)

3. Method `display()`:

   * Displays `x`, `y`, and shared `z`

4. Static method `displayShared()`:

   * Displays only the shared variable `z`
   * Called using class name

---

## 💻 Code

```python id="t9k3xp"
class Sample:
    z = 0  # static (class) variable

    def __init__(self):
        self.x = 0
        self.y = 0

    def setData(self, x, y, z):
        self.x = x
        self.y = y
        Sample.z = z   # class variable updated

    def display(self):
        print(f"x={self.x}\ty={self.y}\tz={Sample.z}")

    @staticmethod
    def displayShared():
        print(f"Shared data : {Sample.z}")


# Main program
s1 = Sample()
s2 = Sample()
s3 = Sample()

s1.setData(10, 20, 30)
s2.setData(40, 50, 60)
s3.setData(70, 80, 90)

s1.display()
s2.display()
s3.display()

Sample.displayShared()
```

---

## ▶️ Example Output

```id="m2k8qx"
x=10	y=20	z=90
x=40	y=50	z=90
x=70	y=80	z=90
Shared data : 90
```

---

## 🧠 Important Concept

* `z` is a **class variable** → shared by all objects
* When updated by any object, it changes for all

👉 Final value of `z = 90` because last update was:

```python
s3.setData(70, 80, 90)
```

---

## 📚 Concepts Used

* Class variable (static variable)
* Instance variables
* Static method (`@staticmethod`)
* Object creation

---

## 🎯 Use Case

This helps you understand:

* Difference between **shared data vs individual data**
* How static variables are used in real applications (e.g., counters, configuration)

---

## ⚠️ Common Mistake

```python
self.z = z   ❌ (creates instance variable)
Sample.z = z ✅ (updates class variable)
```

---

## 🔧 Future Improvements

* Add counter to track number of objects
* Use class method (`@classmethod`)
* Demonstrate real-world example (bank interest rate shared by all accounts)

---

## 📄 License

This project is open-source and free to use.


