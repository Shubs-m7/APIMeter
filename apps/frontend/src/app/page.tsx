import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Separator } from '@/components/ui/separator';
import { APP_CONFIG } from '@/config/app';

export default function HomePage() {
  return (
    <div className="flex min-h-screen items-center justify-center p-4">
      <Card className="w-full max-w-md">
        <CardHeader className="text-center">
          <CardTitle className="text-3xl font-bold tracking-tighter">{APP_CONFIG.name}</CardTitle>
          <CardDescription>Version {APP_CONFIG.version}</CardDescription>
        </CardHeader>
        <CardContent>
          <Separator className="my-4" />
          <div className="space-y-4">
            <div className="flex justify-between">
              <span className="text-muted-foreground">Architecture Status</span>
              <span className="font-medium text-green-500">Initialized</span>
            </div>
            <div className="flex justify-between">
              <span className="text-muted-foreground">Sprint Status</span>
              <span className="font-medium">Sprint 0 (Task 0.3)</span>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
