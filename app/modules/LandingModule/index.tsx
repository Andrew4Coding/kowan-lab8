import { Link } from 'react-router';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '~/components/ui/card';
import { Calculator, Square, Box, Circle, Cylinder } from 'lucide-react';

export const LandingModule = () => {
  const services = [
    {
      title: 'Square Area',
      description: 'Calculate the area of a square',
      icon: Square,
      link: '/square',
    },
    {
      title: 'Cube Surface Area',
      description: 'Calculate the surface area of a cube',
      icon: Box,
      link: '/cube',
    },
    {
      title: 'Circle Area',
      description: 'Calculate the area of a circle',
      icon: Circle,
      link: '/circle',
    },
    {
      title: 'Tube Surface Area',
      description: 'Calculate the surface area of a tube',
      icon: Cylinder,
      link: '/tube',
    },
  ];

  return (
    <main className="container mx-auto px-4 py-8">
      <div className="mb-8 text-center">
        <h1 className="text-3xl font-bold mb-2 flex items-center justify-center gap-2">
          <Calculator className="size-8" />
          Cloud Computing Lab 8
        </h1>
        <p className="text-muted-foreground">Select a calculation service below</p>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
        {services.map((service) => (
          <Link key={service.link} to={service.link} className="block">
            <Card className="hover:shadow-lg transition-shadow cursor-pointer h-full">
              <CardHeader>
                <div className="flex items-center gap-3">
                  <service.icon className="size-6" />
                  <CardTitle>{service.title}</CardTitle>
                </div>
                <CardDescription>{service.description}</CardDescription>
              </CardHeader>
            </Card>
          </Link>
        ))}
      </div>
    </main>
  );
};
