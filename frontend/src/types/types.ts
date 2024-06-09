

export type LogRegError = {
    first_name?: string[];
    last_name?: string[];
    email?: string[];
    password?: string[];
    confirm_password?: string[];
};

export type Category = {
    id: number;
    name: string;
    created_at: string;
    user: number;
}

export type Product = {
    id: number;
    name: string;
    description: string;
    price: number;
    quantity: number;
    image: string;
    category: number;
    created_at: string;
    user: number;
    category_name: string;
}
export type CreateProductFormType = {
    name: string;
    description: string;
    price: number;
    quantity: number;
    image: File | null;
    category: number;
}
export type CreateProductErrors = {
    name?: string[];
    description?: string[];
    price?: string[];
    quantity?: string[];
    image?: string[];
    category?: string[];
}
export type ProductWithCategory = {
    id: number;
    name: string;
    description: string;
    price: string;
    image: string;
    is_approved: boolean;
    category: number;
    category_name: string;
    created_at: Date;
}
export type AllProductsType = {
    category: number;
    created_at: Date;
    description: string;
    id: number;
    image: string;
    is_approved: boolean;
    name: string;
    price: string;
    quantity: number;
    user: number;
    category_name: string;
}
export type User = {
    auth_provider: string;
    date_joined: string;
    email: string;
    first_name: string;
    id: number;
    is_active: boolean;
    is_staff: boolean;
    is_superuser: boolean;
    is_supplier: boolean;
    is_verified: boolean;
    last_name: string;
}
export type Order = {
    created_at: Date;
    id: number;
    product: number;
    quantity: number;
    product_category_name: string;
    product_price: number;
    product_name: string;
    approved: string;
    supplier_name: string;
    supplier_email: string;
    product_image: string;
    client_name: string;
    client_email: string;

}
export type OrderTableType = {
    client_email: string;
    created_at: Date,
    id: number;
    product: number;
    product_name: string;
    product_price: number;
    quantity: number;
    client_name: string;
    approved: string;
};

export type UserType = {
    id: number;
    email: string;
    first_name: string;
    last_name: string;
    auth_provider: string;
    date_joined: Date;
    is_active: boolean;
    is_staff: boolean;
    is_superuser: boolean;
    is_supplier: boolean;
    is_verified: boolean;
};