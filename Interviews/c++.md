# C++知识点

## 构造 vs. 析构

定义一个对象时先调用基类的构造函数，然后调用派生类的构造函数。
析构函数调用的次序是先派生类的析构后基类的析构，正好相反。

## 封装

## 继承

## 多态

多态是对于不同对象接收相同消息时产生不同的动作。C++的多态性具体体现在运行
和编译两个方面：在程序运行时的多态性通过继承和虚函数来体现；在程序编译时多态性
体现在函数和运算符的重载上。

### 重载overload和重写overrided有什么区别？

**重载**：是指允许存在多个同名函数，而这些函数的参数表不同（或许参数个数不同，或许参数类型不同，或许两者都不同）。
**重写**：是指子类重新定义父类虚函数的方法。

重载：对于这两个函数的调用，在编译器间就已经确定了，是静态的。也就是说，它们的地址在编译期就绑定了（早绑定），因此，重载和多态无关。
重写：和多态真正相关。当子类重新定义了父类的虚函数后，父类指针根据赋给它的不同的子类指针，动态的调用属于子类的该函数，这样的函数调用在编译期间是无法确定的（调用的子类的虚函数的地址无法给出）。因此，这样的函数地址是在运行期绑定的（晚绑定）。

## 引用 Reference

引用名是目标变量名的一个别名，它本身不是一种数据类型，因此引用本身不占存储单元，不能
建立数组的引用。

1. 传递引用给函数与传递指针的效果是一样的。
2. 使用引用传递函数的参数，在内存中并没有产生实参的副本，它是直接对实参操作；而使用
一般变量传递函数的参数，当发生函数调用时，需要给形参分配存储单元，形参变量是实参变量
的副本；如果传递的是对象，还将调用拷贝构造函数。因此，当参数传递的数据较大时，用引用
比用一般变量传递参数的效率和所占空间都好。
3. 使用指针作为函数的参数虽然也能达到与使用引用的效果，但是，在被调函数中同样要给形参
分配存储单元，且需要重复使用*指针变量名的形式进行运算。

## Smart Pointers

1. [https://www.geeksforgeeks.org/smart-pointers-cpp/](https://www.geeksforgeeks.org/smart-pointers-cpp/)
2. [https://www.geeksforgeeks.org/auto_ptr-unique_ptr-shared_ptr-weak_ptr-2/](https://www.geeksforgeeks.org/auto_ptr-unique_ptr-shared_ptr-weak_ptr-2/)

```cpp
MyClass *ptr = new MyClass();
ptr->doSomething();
// We must do delete(ptr) to avoid memory leak
```

- Using smart pointers, we can make pointers to work in way that we don’t need to explicitly call delete.
- C++ libraries provide implementations of smart pointers in the form of *auto_ptr*, *unique_ptr*, *shared_ptr* and *weak_ptr*.

### auto_ptr

auto_ptr is a smart pointer that manages an object obtained via new expression and deletes that object when auto_ptr itself is destroyed. 
only one auto_ptr object can own the pointer at any given time i.e. auto_ptr should not be used where copy semantics are needed.

### unique_ptr

std::unique_ptr was developed in C++11 as a replacement for std::auto_ptr.

*unique_ptr* is a new facility with a similar functionality, but with improved security (no fake copy assignments), added features (deleters) 
and support for arrays. It is a container for raw pointers. It explicitly prevents copying of its contained pointer as would happen with 
normal assignment i.e. it allows exactly one owner of the underlying pointer.

There can only be at most one unique_ptr at any one resource and when that unique_ptr is destroyed, the resource is automatically claimed.

```cpp
unique_ptr<A> ptr1 (new A);

// Error: can't copy unique_ptr
unique_ptr<A> ptr2 = ptr1; 
```
But, unique_ptr can be moved using the new move semantics i.e. using std::move() function to transfer ownership of the contained pointer to another unique_ptr.
```cpp
// Works, resource now stored in ptr2
unique_ptr<A> ptr2 = move(ptr1); 
```
Use unique_ptr when you want to have single ownership(Exclusive) of resource. Only one unique_ptr can point to one resource. 


### shared_ptr

A *shared_ptr* is a container for raw pointers. It is a **reference counting ownership model** i.e. it maintains the reference count of its contained pointer in 
cooperation with all copies of the shared_ptr. So, the counter is incremented each time a new pointer points to the resource and decremented 
when destructor of object is called.

Use *shared_ptr* if you want to share ownership of resource . Many shared_ptr can point to single resource. shared_ptr maintains reference count for this propose. 
when all shared_ptr’s pointing to resource goes out of scope the resource is destroyed.

### weak_ptr

A *weak_ptr* is created as a copy of *shared_ptr*. 
It provides access to an object that is owned by one or more shared_ptr instances, but does not participate in reference counting.

When you do want to refer to your object from multiple places – 
for those references for which it’s ok to ignore and deallocate (so they’ll just note the object is gone when you try to dereference). 
