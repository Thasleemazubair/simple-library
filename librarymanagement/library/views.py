from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, BorrowRecord, Member

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.available_copies > 0:
        member = Member.objects.first()  # Placeholder: Replace with logged-in user logic
        BorrowRecord.objects.create(book=book, member=member)
        book.available_copies -= 1
        book.save()
    return redirect('book_list')

def return_book(request, record_id):
    record = get_object_or_404(BorrowRecord, id=record_id)
    record.book.available_copies += 1
    record.book.save()
    record.delete()
    return redirect('book_list')





