
import React, { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Plus, Minus, UtensilsCrossed, ShoppingCart, Receipt } from 'lucide-react';
import { cafeMenu } from '@/data/cafeMenu';

interface OrderItem {
  item: string;
  price: number;
  qty: number;
  total: number;
}

const Index = () => {
  const [orders, setOrders] = useState<OrderItem[]>([]);
  const [showBill, setShowBill] = useState(false);

  const addToOrder = (item: string, price: number) => {
    const existingOrder = orders.find(order => order.item === item);
    if (existingOrder) {
      setOrders(orders.map(order => 
        order.item === item 
          ? { ...order, qty: order.qty + 1, total: (order.qty + 1) * order.price }
          : order
      ));
    } else {
      setOrders([...orders, { item, price, qty: 1, total: price }]);
    }
  };

  const updateQuantity = (item: string, change: number) => {
    setOrders(orders.map(order => {
      if (order.item === item) {
        const newQty = Math.max(1, order.qty + change);
        return { ...order, qty: newQty, total: newQty * order.price };
      }
      return order;
    }).filter(order => order.qty > 0));
  };

  const removeFromOrder = (item: string) => {
    setOrders(orders.filter(order => order.item !== item));
  };

  const getTotalAmount = () => {
    return orders.reduce((total, order) => total + order.total, 0);
  };

  const generateBill = () => {
    setShowBill(true);
  };

  if (showBill) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-orange-50 to-red-50 p-4">
        <div className="max-w-2xl mx-auto">
          <Card className="shadow-lg">
            <CardHeader className="text-center">
              <CardTitle className="flex items-center justify-center gap-2 text-2xl">
                <Receipt className="h-6 w-6" />
                BILL
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <div className="border-b-2 border-dashed pb-2">
                  <div className="grid grid-cols-5 gap-2 font-semibold text-sm">
                    <span className="col-span-2">Item</span>
                    <span className="text-center">Qty</span>
                    <span className="text-center">Price</span>
                    <span className="text-center">Total</span>
                  </div>
                </div>
                
                {orders.map((order, index) => (
                  <div key={index} className="grid grid-cols-5 gap-2 text-sm">
                    <span className="col-span-2">{order.item}</span>
                    <span className="text-center">{order.qty}</span>
                    <span className="text-center">₹{order.price}</span>
                    <span className="text-center">₹{order.total}</span>
                  </div>
                ))}
                
                <div className="border-t-2 border-dashed pt-2">
                  <div className="flex justify-between font-bold text-lg">
                    <span>TOTAL BILL</span>
                    <span>₹{getTotalAmount()}</span>
                  </div>
                </div>
                
                <div className="text-center pt-4">
                  <p className="text-lg font-semibold">Thank you!</p>
                  <Button 
                    onClick={() => { setShowBill(false); setOrders([]); }} 
                    className="mt-4"
                  >
                    New Order
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-orange-50 to-red-50 p-4">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-3 mb-4">
            <UtensilsCrossed className="h-8 w-8 text-orange-600" />
            <h1 className="text-4xl font-bold text-gray-900">Cafe Menu</h1>
          </div>
          <p className="text-xl text-gray-600">Select items and quantities for your order</p>
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          {/* Menu Categories */}
          <div className="lg:col-span-2">
            <div className="grid gap-6">
              {Object.entries(cafeMenu).map(([categoryId, categoryData]) => (
                <Card key={categoryId} className="shadow-lg">
                  <CardHeader>
                    <CardTitle className="capitalize text-orange-700">
                      {categoryData.category}
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="grid md:grid-cols-2 gap-3">
                      {Object.entries(categoryData.items).map(([itemId, itemData]) => (
                        <div key={itemId} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors">
                          <div className="flex-1">
                            <h4 className="font-medium">{itemData.item}</h4>
                            <p className="text-sm text-gray-600">₹{itemData.price}</p>
                          </div>
                          <Button 
                            onClick={() => addToOrder(itemData.item, itemData.price)}
                            size="sm"
                            className="bg-orange-600 hover:bg-orange-700"
                          >
                            Add
                          </Button>
                        </div>
                      ))}
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>

          {/* Order Summary */}
          <div className="space-y-6">
            {orders.length > 0 && (
              <Card className="shadow-lg">
                <CardHeader>
                  <CardTitle className="flex items-center gap-2 text-green-700">
                    <ShoppingCart className="h-5 w-5" />
                    Your Order
                  </CardTitle>
                  <CardDescription>Review and modify your order</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {orders.map((order, index) => (
                      <div key={index} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                        <div className="flex-1">
                          <h4 className="font-medium">{order.item}</h4>
                          <p className="text-sm text-gray-600">₹{order.price} each</p>
                        </div>
                        <div className="flex items-center gap-2">
                          <Button
                            variant="outline"
                            size="sm"
                            onClick={() => updateQuantity(order.item, -1)}
                            disabled={order.qty <= 1}
                          >
                            <Minus className="h-3 w-3" />
                          </Button>
                          <span className="font-semibold w-8 text-center">{order.qty}</span>
                          <Button
                            variant="outline"
                            size="sm"
                            onClick={() => updateQuantity(order.item, 1)}
                          >
                            <Plus className="h-3 w-3" />
                          </Button>
                          <Button
                            variant="destructive"
                            size="sm"
                            onClick={() => removeFromOrder(order.item)}
                            className="ml-2"
                          >
                            Remove
                          </Button>
                        </div>
                      </div>
                    ))}
                    
                    <div className="border-t pt-3">
                      <div className="flex justify-between font-bold text-lg">
                        <span>Total:</span>
                        <span>₹{getTotalAmount()}</span>
                      </div>
                      <Button 
                        onClick={generateBill} 
                        className="w-full mt-3 bg-green-600 hover:bg-green-700"
                        size="lg"
                      >
                        Generate Bill
                      </Button>
                    </div>
                  </div>
                </CardContent>
              </Card>
            )}

            {orders.length === 0 && (
              <Card className="shadow-lg">
                <CardContent className="p-6 text-center">
                  <ShoppingCart className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                  <p className="text-gray-600">Your order is empty</p>
                  <p className="text-sm text-gray-500">Add items from the menu to get started</p>
                </CardContent>
              </Card>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Index;
