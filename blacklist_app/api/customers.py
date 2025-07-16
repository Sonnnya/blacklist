from fastapi import APIRouter
from schemas.customers import Customer, InCustomer
from schemas.reasons import Reason

router = APIRouter(prefix="/blacklist", tags=["Черный список пользователей"])


@router.get("/")
async def get_customers() -> list[Customer]:
    return


@router.get("/")
async def get_customers_paginated() -> list[Customer]:
    return


@router.get("/check_customer/{id}")
async def is_in_blacklist() -> Reason:
    # birthday
    return


@router.post("/")
async def add_customer(customer: InCustomer) -> Customer:
    return customer


@router.post("/")
async def add_customers(customers: list[InCustomer]) -> int:
    return
