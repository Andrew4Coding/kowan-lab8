import { useEffect } from 'react';
import { useFetcher } from 'react-router';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '~/components/ui/card';
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from '~/components/ui/form';
import { Input } from '~/components/ui/input';
import { Button } from '~/components/ui/button';
import { Square } from 'lucide-react';

const squareSchema = z.object({
  side: z.string().min(1, 'Side length is required').refine((val) => !isNaN(Number(val)) && Number(val) > 0, {
    message: 'Side length must be a positive number',
  }),
});

type SquareFormValues = z.infer<typeof squareSchema>;

export const SquareModule = () => {
  const fetcher = useFetcher();
  
  const form = useForm<SquareFormValues>({
    resolver: zodResolver(squareSchema),
    defaultValues: {
      side: '',
    },
  });

  const onSubmit = (data: SquareFormValues) => {
    fetcher.submit(data, { method: 'post' });
  };

  useEffect(() => {
    if (fetcher.data?.success) {
      form.reset();
    }
  }, [fetcher.data]);

  return (
    <main className="container mx-auto px-4 py-8">
      <div className="max-w-md mx-auto">
        <Card>
          <CardHeader>
            <div className="flex items-center gap-3">
              <Square className="size-6" />
              <CardTitle>Square Area Calculator</CardTitle>
            </div>
            <CardDescription>Calculate the area of a square</CardDescription>
          </CardHeader>
          <CardContent>
            <Form {...form}>
              <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
                <FormField
                  control={form.control}
                  name="side"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Side Length</FormLabel>
                      <FormControl>
                        <Input placeholder="Enter side length" type="number" step="any" {...field} />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />
                
                <Button type="submit" disabled={fetcher.state === 'submitting'} className="w-full">
                  {fetcher.state === 'submitting' ? 'Calculating...' : 'Calculate'}
                </Button>

                {fetcher.data?.result && (
                  <div className="mt-4 p-4 bg-muted rounded-md">
                    <p className="text-sm font-medium">Result:</p>
                    <p className="text-2xl font-bold">{fetcher.data.result} square units</p>
                  </div>
                )}
              </form>
            </Form>
          </CardContent>
        </Card>
      </div>
    </main>
  );
};
